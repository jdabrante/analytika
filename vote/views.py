from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render

from choice.models import Choice
from poll.models import Poll

from .models import Vote


def vote_choice(request: HttpRequest, poll_id) -> HttpResponse:
    poll = get_object_or_404(Poll, id=poll_id)
    pass
    # poll = get_object_or_404(Poll, id=poll_id)
    # choice = get_object_or_404(Choice, name=request.POST[poll.name])
    # new_vote = Vote(poll=poll, choice=choice)
    # new_vote.save()
    # votes = Vote.objects.filter(poll=poll)
    # results = {}
    # total_votes = 0
    # for vote in votes:
    #     if vote.choice not in results:
    #         results[vote.choice] = 1
    #         total_votes += 1
    #     else:
    #         results[vote.choice] += 1
    #         total_votes += 1

    # for key in results.keys():
    #     results[key] = {'votes': results[key], 'percentaje': (results[key] * 100 / total_votes)}

    # return render(
    #     request, 'vote/results.html', dict(votes=votes, results=results, total_votes=total_votes)
    # )
