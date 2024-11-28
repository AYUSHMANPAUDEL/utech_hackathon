from django.contrib import admin
from django.urls import path , include
from navigator_helper import views
urlpatterns = [
path("map/",views.navigate_map ,name="map_navigation"),
path("trip/<int:id>",views.trip_plan, name="trip_page"),
]
