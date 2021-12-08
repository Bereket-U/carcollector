from django.db.models import fields
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Car



def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

# Add new view
def cars_index(request):
    cars = Car.objects.all()
    return render(request, 'cars/index.html', { 'cars': cars })

def cars_detail(request, car_id):
    car = Car.objects.get(id = car_id)
    return render(request, 'cars/detail.html', {'car': car})

class CarCreate(CreateView):
    model = Car
    fields = '__all__'

class CarUpdate(UpdateView):
    model = Car
    fields = ['model','year', 'description']

class CarDelete(DeleteView):
    model = Car
    success_url = '/cars/'