from django.urls import path

from . import views

app_name = 'flashcards'
urlpatterns = [
    path('', views.index, name='index'),
    path('action', views.action, name='action')
]