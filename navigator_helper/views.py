from django.shortcuts import render

# Create your views here.
def navigate_map(request):
    return render(request,"navigator_helper/map.html")