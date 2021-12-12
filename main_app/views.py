from django.db.models import fields
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Car, Accessory
from .forms import ServiceForm


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
    accessories_car_doesnt_have = Accessory.objects.exclude(id__in = car.accessories.all().values_list('id'))
    service_form = ServiceForm()
    return render(request, 'cars/detail.html', {'car': car, 'service_form': service_form, 'accessories': accessories_car_doesnt_have})

def add_service(request, car_id):
    pass

def add_service(request, car_id):
  form = ServiceForm(request.POST)
  if form.is_valid():
    new_service = form.save(commit=False)
    new_service.car_id = car_id
    new_service.save()
  return redirect('detail', car_id=car_id)

class CarCreate(CreateView):
    model = Car
    fields = '__all__'

class CarUpdate(UpdateView):
    model = Car
    fields = ['model','year', 'description']

class CarDelete(DeleteView):
    model = Car
    success_url = '/cars/'

#acc
class AccessoryList(ListView):
  model = Accessory

class AccessoryDetail(DetailView):
  model = Accessory

class AccessoryCreate(CreateView):
  model = Accessory
  fields = '__all__'

class AccessoryUpdate(UpdateView):
  model = Accessory
  fields = ['name']

class AccessoryDelete(DeleteView):
  model = Accessory
  success_url = '/accessories/'

def assoc_accessory(request, car_id, accessory_id):
  Car.objects.get(id=car_id).accessories.add(accessory_id)
  return redirect('detail', car_id=car_id)