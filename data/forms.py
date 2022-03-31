from django import forms
from .models import Restaurant, RestaurantReview

class addRestaurant(forms.ModelForm):

    class Meta:
        model = Restaurant
        fields = '__all__'

class editRestaurant(forms.ModelForm):

    class Meta:
        model = Restaurant
        fields = '__all__'
