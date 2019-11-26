from django.urls import path
from .apiviews import PollList, PollDetail

from . import views

app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path('', PollList.as_view(), name='index'),
    # ex: /polls/5/
    path('<int:pk>/', PollDetail.as_view(), name='detail'),
]
