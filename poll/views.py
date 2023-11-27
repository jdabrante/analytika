from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import  Poll


def polls_list(request: HttpRequest) -> HttpResponse:
    polls = Poll.objects.all()
    return render(request, 'polls/polls_list.html', dict(polls=polls))


def poll_detail(request: HttpRequest, poll_id: int) -> HttpResponse:
    poll = get_object_or_404(Poll, id=poll_id)
    return render(request, 'polls/poll_detail.html', dict(poll=poll))
