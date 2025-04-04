# Snake and Ladder - Django Edition

A modern, single-player implementation of the classic Snake and Ladder board game built with Python and Django. This project features a professional UI, session-based gameplay, high score tracking, and a simple username entry system to start the game.

---

## 📌 Table of Contents
- [Features](#features)
- [Screenshots](#screenshots)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)
- [Notes for Customization](#notes-for-customization)

---

## 🎮 Features
- **Start Page:** Enter a username to begin the game.
- **Gameplay:** Roll a die to move across a **10x10 board** with snakes and ladders.
- **High Scores:** Tracks and displays the **top 5 scores** (fewest moves) in the database.
- **Professional UI:** Responsive design with animations (dice roll, confetti on win) and a clean layout.
- **Session Management:** Uses Django sessions to maintain game state without requiring user login.
- **Visual Feedback:** Snakes (**red**), ladders (**green**), and player position (**yellow**) are visually distinct.
- **Real-time Messages:** Get feedback on moves, snake bites, ladder climbs, and wins.

---

## ⚙️ Installation

### Prerequisites
- **Python 3.8+**
- **Git**
- **Virtualenv** *(optional but recommended)*

### Steps
1️⃣ Clone the Repository:
   ```bash
   git clone https://github.com/yourusername/snake-ladder-django.git
   cd snake-ladder-django
   ```
2️⃣ Set Up a Virtual Environment *(Optional)*:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3️⃣ Install Dependencies:
   ```bash
   pip install django
   ```
4️⃣ Apply Migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
5️⃣ Run the Development Server:
   ```bash
   python manage.py runserver
   ```
   Open your browser and visit: **http://127.0.0.1:8000/**

---

## 🕹️ Usage
- **Start the Game:**
  - Go to the homepage (`/`) and enter a username.
  - Click **"Start Game"** to proceed to the game board.
- **Play:**
  - Click **"Roll Die"** to move your piece.
  - Watch for **snakes (slide down)** and **ladders (climb up)**.
  - Reach **position 100** to win!
- **View High Scores:**
  - The **Top 5 scores** are displayed on the game page after each move.
- **New Game:**
  - Click **"New Game"** to reset and return to the start page.

---

## 📂 Project Structure
```
snake_ladder/
├── game/
│   ├── migrations/         # Database migrations
│   ├── templates/
│   │   └── game/
│   │       ├── board.html  # Main game interface
│   │       └── start.html  # Username entry page
│   ├── __init__.py
│   ├── apps.py
│   ├── models.py          # GameRecord model for high scores
│   ├── urls.py            # App-specific URL routes
│   └── views.py           # Game logic and views
├── snake_ladder/
│   ├── __init__.py
│   ├── settings.py        # Project settings
│   ├── urls.py            # Project URL configuration
│   └── wsgi.py            # WSGI entry point
└── manage.py              # Django management script
```

---

## 🛠️ Technologies Used
- **Django 4.2** - Web framework for Python.
- **Python 3.8+** - Core programming language.
- **SQLite** - Default database for storing high scores.
- **HTML/CSS/JavaScript** - Frontend with custom styling and animations.
- **Google Fonts** - Roboto font for a professional look.

---

## 🤝 Contributing
Contributions are welcome! Follow these steps:

1. **Fork** the repository.
2. **Create a new branch**: `git checkout -b feature/your-feature`
3. **Make your changes** and commit: `git commit -m "Add your feature"`
4. **Push to your branch**: `git push origin feature/your-feature`
5. **Open a Pull Request**.

✅ Please ensure your code follows **PEP 8** style guidelines and includes appropriate comments.

---

## 📜 License
This project is licensed under the **MIT License**. See the `LICENSE` file for details.

---

## 📝 Notes for Customization
- Replace `yourusername` in the clone URL with your actual GitHub username.
- Add real screenshots by capturing your app and uploading them to the repo (e.g., in a `screenshots/` folder).
- If you add more features *(e.g., multiplayer, custom themes)*, update the **Features** section accordingly.

---

🚀 **Happy Coding & Have Fun Playing!** 🎲🐍🔼
