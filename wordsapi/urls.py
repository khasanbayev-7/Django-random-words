from django.urls import path
from .views import random_words_view

urlpatterns = [
    path('random-words/', random_words_view, name='random-words'),
]
