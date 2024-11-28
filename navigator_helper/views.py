from django.shortcuts import render , get_object_or_404
from map_roadmap.models import Trips
def navigate_map(request):
    schedule = {
        "day1": [
            {"location": "Kathmandu Durbar Square", "status": "False", "latitude": 27.7045, "longitude": 85.3076},
            {"location": "Thamel", "status": "False", "latitude": 27.7112, "longitude": 85.3002},
            {"location": "Swayambhunath Stupa", "status": "False", "latitude": 27.7149, "longitude": 85.2904}
        ],
        "day2": [
            {"location": "Pashupatinath Temple", "status": "False", "latitude": 27.6676, "longitude": 85.4098},
            {"location": "Boudhanath Stupa", "status": "False", "latitude": 27.7131, "longitude": 85.3603},
            {"location": "Garden of Dreams", "status": "False", "latitude": 27.7116, "longitude": 85.2955}
        ],
        "day3": [
            {"location": "Bhaktapur Durbar Square", "status": "False", "latitude": 27.6689, "longitude": 85.4278},
            {"location": "Patan Durbar Square", "status": "False", "latitude": 27.6669, "longitude": 85.3241},
            {"location": "Himalayan Java Coffee", "status": "False", "latitude": 27.7061, "longitude": 85.2923}
        ]
    }
    return render(request, "navigator_helper/map.html", {"schedule": schedule})

def trip_plan(request,id):
    trip = get_object_or_404(Trips,id=id)
    if trip:
        return render(request,"navigator_helper/trip_setup.html",{"trip":trip})
    return render(request,"navigator_helper/trip_setup.html",{"error":"Error Occured"})