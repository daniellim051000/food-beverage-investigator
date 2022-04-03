from django import forms
from .models import Restaurant

class addRestaurant(forms.ModelForm):
    restaurant_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Please enter restaurant name.'}), label='Restaurant Name')
    restaurant_type = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Please enter restaurant type.'}), label='Restaurant Type')
    address = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Please enter full address.'}), label='Address')
  
    class Meta:
        model = Restaurant
        fields = ('restaurant_name', 'restaurant_type', 'address', 
        'online_order', 'booking', 'pricing_level', 'hygiene_level', 'average_serving', 'latitude', 'longitude')

class editRestaurant(forms.ModelForm):
    restaurant_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Please enter restaurant name.'}), label='Restaurant Name')
    restaurant_type = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Please enter restaurant type.'}), label='Restaurant Type')
    address = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Please enter full address.'}), label='Address')
  
    class Meta:
        model = Restaurant
        fields = ('restaurant_name', 'restaurant_type', 'address', 
        'online_order', 'booking', 'pricing_level', 'hygiene_level', 'average_serving', 'latitude', 'longitude')
