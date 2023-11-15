from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("rounds/", views.rounds, name="rounds"),
    path("results/", views.results, name="results"),
]