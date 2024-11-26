from django.shortcuts import render

def navigate_map(request):
    schedule = [
        {"name": "Kathmandu Durbar Square", "latitude": 27.7045, "longitude": 85.3076},
        {"name": "Swayambhunath Stupa", "latitude": 27.7149, "longitude": 85.2903},
        {"name": "Pashupatinath Temple", "latitude": 27.7104, "longitude": 85.3488},
    ]
    return render(request, "navigator_helper/map.html", {"schedule": schedule})
