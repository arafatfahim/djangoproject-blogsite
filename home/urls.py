from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('contact', views.contact, name="Contact"),
    path('about', views.about, name="About"),
    path('', views.home, name="Home"),
    path('search', views.search, name="Search"),
    path('signup', views.handlesignup, name="Signup"),
    path('login', views.handlelogin, name="Login"),
    path('logout', views.handlelogout, name="Logout"),

] 
#python manage.py migrate --run-syncdb