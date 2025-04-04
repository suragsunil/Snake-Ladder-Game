from django.shortcuts import render, redirect
from django.contrib import messages
from .models import GameRecord
import random

def start_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        if username:
            request.session['username'] = username
            request.session['position'] = 1
            request.session['moves'] = 0
            request.session['completed'] = False
            request.session['last_roll'] = 0
            return redirect('game_view')
        else:
            messages.error(request, "Please enter a username!")
    return render(request, 'start.html')

def game_view(request):
    if 'username' not in request.session:
        return redirect('start_view')

    # Define snakes and ladders
    SNAKES = {
        16: 6, 28: 8, 47: 26, 56: 53, 62: 19,
        64: 60, 87: 24, 93: 73, 95: 75, 98: 79
    }
    LADDERS = {
        1: 38, 4: 14, 9: 31, 21: 42, 28: 84,
        51: 67, 71: 91, 80: 100
    }

    if request.method == 'POST' and not request.session['completed']:
        roll = random.randint(1, 6)
        request.session['last_roll'] = roll
        request.session['moves'] += 1
        new_position = request.session['position'] + roll

        if new_position <= 100:
            if new_position in SNAKES:
                request.session['position'] = SNAKES[new_position]
                messages.warning(request, f"Snake bit you! Slid from {new_position} to {request.session['position']}")
            elif new_position in LADDERS:
                request.session['position'] = LADDERS[new_position]
                messages.success(request, f"Climbed ladder from {new_position} to {request.session['position']}!")
            else:
                request.session['position'] = new_position
                messages.info(request, f"Moved forward to {request.session['position']} (Rolled: {roll})")

            if request.session['position'] == 100:
                request.session['completed'] = True
                GameRecord.objects.create(
                    username=request.session['username'],
                    moves=request.session['moves']
                )
                messages.success(request, f"Congratulations, {request.session['username']}! You won in {request.session['moves']} moves!")
        else:
            messages.info(request, f"Rolled {roll} - Need {100 - request.session['position']} or less to win!")
        
        request.session.modified = True

    high_scores = GameRecord.objects.all()[:5]  # Top 5 high scores
    context = {
        'username': request.session['username'],
        'position': request.session['position'],
        'moves': request.session['moves'],
        'last_roll': request.session['last_roll'],
        'completed': request.session['completed'],
        'snakes': SNAKES,
        'ladders': LADDERS,
        'high_scores': high_scores,
    }
    return render(request, 'board.html', context)

def new_game(request):
    if 'username' in request.session:
        del request.session['username']  # Clear username to force start page
    request.session.flush()
    messages.success(request, "New game started!")
    return redirect('start_view')