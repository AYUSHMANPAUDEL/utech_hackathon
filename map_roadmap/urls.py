from django.contrib import admin
from django.urls import path , include
from map_roadmap import views
urlpatterns = [
    path("dashboard/", views.dashboard ,name="dashboard_page"),
    path("save_trip/",views.save_trip,name="save_trip_page"),



]