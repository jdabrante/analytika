from django.db import models

from poll.models import Poll


class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='choices')
    name = models.CharField(max_length=100)

    def get_percentaje(self):
        # Esto puede ser la clave
        total = Poll.objects.all()

    def __str__(self):
        return self.name
