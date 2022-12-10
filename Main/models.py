from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=150)
    position = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to="Team_pictures")
    

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    name = models.CharField(max_length=150)
    position = models.CharField(max_length=150)
    comment = models.TextField()
    image = models.ImageField(upload_to="Testimonial_pictures")
    

    def __str__(self):
        return self.name






