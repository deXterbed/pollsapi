from django.urls import path
from .apiviews import PollList, PollDetail, ChoiceList, CreateVote

from . import views

app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path('polls/', PollList.as_view(), name='index'),
    # ex: /polls/5/
    path('polls/<int:pk>/', PollDetail.as_view(), name='detail'),
    path("choices/", ChoiceList.as_view(), name="choice_list"),
    path("vote/", CreateVote.as_view(), name="create_vote"),
]
