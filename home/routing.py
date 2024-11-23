from django.urls import path
from . import consumers


websocket_urlpatterns =[
  path('ws/alert/<str:userId>/',consumers.my_consumer.as_asgi()),
]