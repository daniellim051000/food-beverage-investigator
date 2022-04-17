from django.shortcuts import redirect, render
from django.contrib import messages
from data.forms import addRestaurant
from data.models import Restaurant

# Create your views here.
def add_restaurant(request):
    if request.method == "POST":
        form = addRestaurant(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            messages.success(request, 'Restaurant added successfully!')
            return redirect('home')
        else:
            messages.error(request, "Error, Failed to add restaurant!")
    else:
        form = addRestaurant()
    return render(request, "add_restaurant.html", {'form': form})


    return redirect('home')

def list_restaurant(request):
    queryset = Restaurant.objects.all()

    context = {
        'form' : queryset
    }     
    return render(request, "list_restaurant.html", context)

def add_review(request):

    return render(request, "add_review.html")