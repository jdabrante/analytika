from django.contrib import admin
from .models import Choice

@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['name']
