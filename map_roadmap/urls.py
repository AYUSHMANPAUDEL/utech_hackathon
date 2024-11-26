from django.contrib import admin
from django.urls import path , include
from map_roadmap import views
urlpatterns = [
    path("explore", views.explore ,name="explore")


]