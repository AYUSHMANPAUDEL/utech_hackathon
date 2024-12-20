from django.contrib import admin
from django.urls import path , include
from navigator_helper import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
path("map/",views.navigate_map ,name="map_navigation"),
path("trip/<int:id>",views.trip_plan, name="trip_page"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)