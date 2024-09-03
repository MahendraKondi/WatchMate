from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

class Streamplatform(models.Model):
    name = models.CharField(max_length=50)
    about = models.CharField(max_length=200)
    website = models.URLField(max_length=50)

    def __str__(self):
        return self.name


class Watchlist(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=200)
    active = models.BooleanField(default=True)
    platform = models.ForeignKey(Streamplatform,on_delete=models.CASCADE,related_name= "watchlist")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class Review(models.Model):
    review_user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    description = models.CharField(max_length=200)
    watchlist = models.ForeignKey(Watchlist,on_delete=models.CASCADE,related_name="reviews")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True) 


    def __str__(self):
        return str(self.rating) + "  " + self.watchlist.title