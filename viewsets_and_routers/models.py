from django.db import models

# Create your models here.
class Cricket(models.Model):
    player_name = models.CharField(max_length=100)
    team_name = models.CharField(max_length=100)
    runs_scored = models.IntegerField()
    wickets_taken = models.IntegerField()
    match_date = models.DateField()

    class Meta:
        ordering = ['match_date']

    def __str__(self):
        return f"{self.player_name} - {self.team_name} ({self.match_date})"