from django.urls import path
from . import views

app_name = 'poll'

urlpatterns = [
    path('polls/', views.polls_list, name='polls_list'),
    path('poll/<int:poll_id>', views.poll_detail, name='poll_detail'),
]
