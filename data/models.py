from tkinter import CASCADE
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import uuid
# Create your models here.

PRICE = (
    ('< RM50','< RM50'),
    ('RM51 - RM100','RM51 - RM100'),
    ('RM101 - RM200','RM101 - RM200'),
    ('> RM200','> RM200'),
)

HYGIENE = (
    ('0','0'),
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
)

SERVING = (
    ('< 15','< 15'),
    ('15 - 30','15 - 30'),
    ('30 - 45','30 - 45'),
    ('45 - 60','45 - 60'),
    ('> 60','> 60'),
)

class Restaurant(models.Model):
    restaurant_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    restaurant_name = models.CharField(max_length=250, unique=False, blank=False)
    address = models.CharField(max_length=300, unique=False, blank=False)
    retaurant_type = models.CharField(max_length=50, unique=False, blank=False)
    online_order = models.BooleanField(default=False)
    booking = models.BooleanField(default=False)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, default=0)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, default=0) 
    pricing_level = models.CharField('Price Level (For One Person)', max_length=20, choices=PRICE, default="Cheap")
    hygiene_level = models.CharField('Hygiene Level', max_length=5, choices=HYGIENE, default="< RM50")
    average_serving = models.CharField('Average Serving Time', max_length=5, choices=SERVING, default="< 15")
    average_rating = models.FloatField(default=0.0, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    total_rating = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.restaurant_name

class RestaurantReview(models.Model):
    review_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    restaurant = models.ForeignKey(Restaurant, related_name="restaurant", on_delete=models.SET_NULL, null=True)
    review = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.restaurant