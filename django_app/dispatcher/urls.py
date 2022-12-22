from django.urls import path

from . import views

app_name = 'dispatcher'
urlpatterns = [
    path('', views.index, name='index')
]
