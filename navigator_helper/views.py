from django.shortcuts import render, get_object_or_404
from map_roadmap.models import Trips
from django.http import JsonResponse
from navigator_helper.models import Hotels
import math

# Helper function to calculate distance between two points
def haversine(lat1, lon1, lat2, lon2):
    # Radius of the Earth in kilometers
    R = 6371
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    
    a = math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) * math.sin(dlon / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c  # in kilometers
    return distance

# Navigate map view
def navigate_map(request):
    latitude = request.GET.get('latitude', 27.7172)  # Default to Kathmandu, Nepal
    longitude = request.GET.get('longitude', 85.3240)
    return render(request, "navigator_helper/map.html", {"latitude": latitude, "longitude": longitude})

# Update trip_plan view
def trip_plan(request, id):
    trip = get_object_or_404(Trips, id=id)
    hotel_details = None

    if not trip.hotel_status:  # Only show hotel details if hotel status is False
        nearest_hotels = []

        # Extract latitudes and longitudes from the trip_json
        for day, events in trip.trip_json.items():
            for event in events:
                latitude = event.get('latitude')
                longitude = event.get('longitude')

                if latitude and longitude:
                    # Loop through the hotels in the database and find nearby hotels
                    hotels = Hotels.objects.all()  # Get all hotels in the database
                    for hotel in hotels:
                        # Use the corrected 'latitude' and 'longitude' fields from the Hotels model
                        distance = haversine(latitude, longitude, float(hotel.latitude), float(hotel.longitude))
                        if distance <= 5:  # Assuming we want hotels within a 5 km radius
                            nearest_hotels.append({
                                'name': hotel.name,
                                'rating': hotel.rating,
                                'distance': distance,
                                'hotel_image1': hotel.hotel_image1.url,  # Include hotel images
                                'hotel_image2': hotel.hotel_image2.url,
                                'hotel_image3': hotel.hotel_image3.url,
                            })
                    if nearest_hotels:  # If we found hotels, stop searching further
                        break
            if nearest_hotels:
                break  # Exit the loop if hotels are found

        hotel_details = nearest_hotels if nearest_hotels else None

    return render(request, 'navigator_helper/trip_setup.html', {'trip': trip, 'hotel_details': hotel_details})
