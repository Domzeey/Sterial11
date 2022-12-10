from django.urls import path
from .views import home_page, about, services, blog, contact, single



urlpatterns = [
    path("", home_page, name="home"),
    path("about", about, name="about"),
    path("services", services, name="services"),
    path("blog", blog, name="blog"),
    path("contact", contact, name="contact"),
    path("single", single, name="single"),
]