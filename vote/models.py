from django.db import models
from poll.models import Poll
from choice.models import Choice

class Vote(models.Model):
    vote_at = models.DateTimeField(auto_now=True)
    poll = models.ForeignKey(Poll, related_name='votes', on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, related_name='votes', on_delete=models.CASCADE)
