from django.db import models

class Score(models.Model):
    score = models.IntegerField()
    pseudo = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)
