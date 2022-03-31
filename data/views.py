from django.shortcuts import redirect, render

# Create your views here.
def add_restaurant(request):
    
    return redirect('home')

def list_restaurant(request):
    return render(request, "restaurant_list.html")