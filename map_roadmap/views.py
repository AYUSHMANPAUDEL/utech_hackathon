from django.shortcuts import render
import openai
# Create your views here.
def dashboard(request):
    return render (request, "map_roadmap/dashboard.html")


def plan_trip(current_location,destination, days, member):
    OPENAI_API_KEY = "..."  # Replace with your actual OpenAI API key

    openai.api_key = OPENAI_API_KEY

    prompt = f"""
    You are a specialist trip planner. You know every location about Nepal places. Please help me plan a trip for me.My current location is {current_location}.
    I would like to visit {destination} of Nepal for {days} days. There are {member} people with us. 
    Just make me a proper trip plan in JSON format like:
    {{
    "day1": [
        {"location": "Kathmandu Durbar Square", "status": "False","latitude": 27.7045, "longitude": 85.3076},
        {"location": "Thamel", "status": "False" , "latitude": ...., "longitude": ....}
    ],
    }}
    The status of each location should be 'False' because it is the first time visiting those locations. Just reply me with JSON format nothing other.There can be more than one location
    in oneday just make sure that the distance and time taken in one place normally will be enough to go to another place.
    """

    completion = openai.ChatCompletion.create(
        model="gpt-4",  # You can change this to a different model if needed
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return completion['choices'][0]['message']['content']