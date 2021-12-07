from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

class Car:
    def __init__(self, make, model, year, description):
        self.make = make
        self.model = model
        self.year = year
        self.description = description
    
cars = [
     Car('Audi', 'Q5', '2022', '2022 Audi Q5 2.0T quattro Premium Plus S Line AWD'),
     Car('Hyundai', 'Elantra', '2021', 'Amazing car'),
     Car('Hyundai', 'Accent', '2022', 'Hyundai Accent Preferred Hatchback FWD'),
]


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

# Add new view
def cars_index(request):
  return render(request, 'cars/index.html', { 'cars': cars })