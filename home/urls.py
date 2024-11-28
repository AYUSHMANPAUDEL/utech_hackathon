from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
     path('admin/', admin.site.urls),
   path("home",views.home_page,name="home_page"),
   path("",views.register_page,name="register_page"),
   path("login",views.login_page,name="login_page"),
   path("logout",views.logout_page,name="logout_page"),
  
]
