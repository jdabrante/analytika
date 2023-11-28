from django.db import models
from django.urls import reverse


class Poll(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200)
    active = models.BooleanField()
    opened_from = models.DateTimeField()
    opened_to = models.DateTimeField()

    def get_absolute_url(self):
        return reverse("poll:poll_detail", args=[self.id])

    def __str__(self):
        return self.name
