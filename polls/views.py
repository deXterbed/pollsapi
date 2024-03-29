from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from .models import Poll

def list(request):
    MAX_OBJECTS = 20
    polls = Poll.objects.all()[:MAX_OBJECTS]
    data = {"results": []}
    for poll in polls:
        data["results"].append({
            "question": poll.question,
            "created_by": poll.created_by.username,
            "pub_date": poll.pub_date
        })
    return JsonResponse(data)

def detail(request, pk):
    poll = get_object_or_404(Poll, pk=pk)
    data = {
        "results": {
            "question": poll.question,
            "created_by": poll.created_by.username,
            "pub_date": poll.pub_date
        }
    }
    return JsonResponse(data)
