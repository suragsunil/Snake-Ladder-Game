from django.db import models

class GameRecord(models.Model):
    username = models.CharField(max_length=50)
    moves = models.IntegerField()
    completed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['moves']  # Order by moves (ascending) for high scores

    def __str__(self):
        return f"{self.username} - {self.moves} moves"