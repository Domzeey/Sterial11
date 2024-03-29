from django.shortcuts import render, redirect
from .models import Team, Testimonial, Destination, Recent_post


# Create your views here.

def home_page(request):
    testimonial = Testimonial.objects.all()
    destination = Destination.objects.all()
    recentpost = Recent_post.objects.all()
    context = {
        "testimonial" : testimonial,
        "destination" : destination,
        "recentpost" : recentpost
    }
    return render(request, "Main/index.html", context)

def about(request):
    team = Team.objects.all() 
    context = {
        "team" : team
    }
    return render(request, "Main/about.html", context)

def services(request):
    return render(request, "Main/services.html")

def blog(request):
    return render(request, "Main/blog.html")

def contact(request):
    return render(request, "Main/contact.html")

def single(request):
    return render(request, "Main/single.html")

def single_destination(request):
    return render(request, "Main/single_destination.html")