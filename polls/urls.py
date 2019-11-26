from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path('', views.list, name='index'),
    # ex: /polls/5/
    path('<int:pk>/', views.detail, name='detail'),
]
