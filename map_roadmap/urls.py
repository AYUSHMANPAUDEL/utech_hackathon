from django.contrib import admin
from django.urls import path , include
from map_roadmap import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("dashboard/", views.dashboard ,name="dashboard_page"),
    path("save_trip/",views.save_trip,name="save_trip_page"),
    path("dashboard/translator",views.translator,name ="translator_page"),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)