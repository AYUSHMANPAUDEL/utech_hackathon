from django.shortcuts import render , get_object_or_404
from map_roadmap.models import Trips
def navigate_map(request):
    latitude = request.GET.get('latitude', 27.7172)  # Default to Kathmandu, Nepal
    longitude = request.GET.get('longitude', 85.3240)
    return render(request, "navigator_helper/map.html", {"latitude":latitude,"longitude":longitude})

def trip_plan(request,id):
    trip = get_object_or_404(Trips,id=id)
    print(trip.trip_json)
    if trip and trip.username == request.user:
        return render(request,"navigator_helper/trip_setup.html",{"trip":trip})
    return render(request,"navigator_helper/trip_setup.html",{"error":"Error Occured"})