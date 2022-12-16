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
    image = models.FileField()
    

    def __str__(self):
        return self.name


class Destination(models.Model):
    title = models.CharField(max_length=150)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    description = models.TextField()
    image = models.ImageField(upload_to="Destination_pictures")


    def __str__(self):
        return self.title






