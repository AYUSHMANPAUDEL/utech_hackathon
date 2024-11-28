from django.shortcuts import render , get_object_or_404
from map_roadmap.models import Trips


def navigate_map(request,id):
    trip = get_object_or_404(Trips, id=id)
    schedule = trip.trip_json
    if not schedule:
        # Handle the case where the schedule is empty or invalid
        return render(request, "navigator_helper/map.html", {"error": "No schedule data found for this trip."})
    return render(request, "navigator_helper/map.html", {"schedule": schedule})
