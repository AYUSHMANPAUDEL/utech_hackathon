from django.shortcuts import render , HttpResponse , redirect
from map_roadmap.models import Trips
import g4f
import asyncio
import json

# Set asyncio event loop policy for Windows (necessary for some async operations)
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

def dashboard(request):
    trips = Trips.objects.filter(username=request.user)
    if request.method == 'POST':
        # Get data from the form
        current_location = request.POST.get('current_location')
        destination = request.POST.get('destination')
        duration = request.POST.get('duration')
        members = request.POST.get('members')
        
        # Get the trip plan from the AI model
        planned_trip = plan_trip(current_location, destination, duration, members)
        
        # If the planned trip was successfully returned and is in JSON format, parse it
        try:
            planned_trip_json = json.loads(planned_trip)  # Parsing the JSON response
        except json.JSONDecodeError:
            planned_trip_json = {}  # In case there is an error in parsing

        # Render the response with the planned trip and existing trips
        return render(request, "map_roadmap/dashboard.html", {
            "planned_trip": planned_trip_json, 
            "trips": trips
        })
    
    # If there are existing trips, render them
    if trips.exists():
        return render(request, "map_roadmap/dashboard.html", {"trips": trips})
    
    # If no trips exist, show an error message
    return render(request, "map_roadmap/dashboard.html", {"Error": "No Trips"})

def plan_trip(current_location, destination, duration, members):
    prompt = f"""
        You are a specialist trip planner. You know every location about Nepal places. Please help me plan a trip for me. My current location is {current_location}.
        I would like to visit {destination} of Nepal for {duration} days. There are {members} people with us. 
        Just make me a proper trip plan in JSON format like:
        {{
        "day1": [
            {{"location": "Kathmandu Durbar Square", "status": "False", "latitude": 27.7045, "longitude": 85.3076}},
            {{"location": "Thamel", "status": "False", "latitude": 27.715, "longitude": 85.300}}
        ],
        "day2": [
            {{"location": "Sauraha", "status": "False", "latitude": 27.5891, "longitude": 84.4924}}
        ]
        }}
        The status of each location should be 'False' because it is the first time visiting those locations. Just reply me with JSON format, nothing other than that—not even "```json" . Make sure that there can be more than two or three locations in one day, but make sure the distance and time taken at one place should normally be enough to go to another place.
    """

    response = g4f.ChatCompletion.create(
        model="gpt-4o",
        provider=g4f.Provider.ChatGptEs,
        messages=[{"role": "user", "content": prompt}],
        stream=True,
    )

    trip_plan = ""
    for message in response:
        # Since message is a string, append it directly to trip_plan
        trip_plan += message

    if trip_plan:
        return trip_plan  # Return the full aggregated response
    return False

def save_trip(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            planned_trip = request.POST.get('planned_trip').strip()  # Remove leading/trailing spaces
            
            # Log the received trip data for debugging
            # Replace single quotes with double quotes to ensure valid JSON
            planned_trip = planned_trip.replace("'", '"')
            
            # Check if the data is in valid JSON format
            try:
                planned_trip_json = json.loads(planned_trip)
                planned_trip_json = conver_to_real_json(planned_trip_json)
                Trips.objects.create(username=request.user, trip_json=planned_trip_json)
                return redirect("dashboard_page")
            except json.JSONDecodeError as e:
                # Log the error message and the invalid data for further inspection
                return HttpResponse(f"Error: Invalid JSON format. Please check the input.")
    return HttpResponse("ERROR OCCURRED")


def conver_to_real_json(trip2_json):
    trip1_json = {}

    for day, events in trip2_json.items():
        # If the day's data is already a list, keep it as-is
        if isinstance(events, list):
            trip1_json[day] = [
                {
                    "location": event.get("location", "Unknown Location"),
                    "latitude": event.get("latitude", "Not Provided"),
                    "longitude": event.get("longitude", "Not Provided"),
                    "status": event.get("status", None),
                }
                for event in events
            ]
        # If the day's data is a single dictionary, wrap it in a list
        elif isinstance(events, dict):
            trip1_json[day] = [
                {
                    "location": events.get("location", "Unknown Location"),
                    "latitude": events.get("latitude", "Not Provided"),
                    "longitude": events.get("longitude", "Not Provided"),
                    "status": events.get("status", None),
                }
            ]
        # If no valid data, use an empty list
        else:
            trip1_json[day] = []

    return trip1_json

    
def translator(request):
    return render(request,"map_roadmap/translator.html")