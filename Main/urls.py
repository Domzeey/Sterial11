from django.urls import path
from .views import home_page, about, services, blog, contact, single, single_destination



urlpatterns = [
    path("", home_page, name="home"),
    path("about", about, name="about"),
    path("services", services, name="services"),
    path("blog", blog, name="blog"),
    path("contact", contact, name="contact"),
    path("single", single, name="single"),
    path("single_destination", single_destination, name="single_destination")
]