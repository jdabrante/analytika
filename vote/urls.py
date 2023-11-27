from django.urls import path
from . import views
app_name = 'vote'

urlpatterns = [
    path('/<int:poll_id>', views.vote_choice, name='vote_choice')
]
