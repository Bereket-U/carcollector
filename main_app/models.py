from django.db import models
from django.db.models.deletion import CASCADE
from django.urls import reverse
from django.contrib.auth.models import User

SERVICES = (
  ('BS', 'Basic Service'),
  ('OC', 'Oil Change'),
  ('RAF', 'Replace air filter'),
  ('BR', 'Battery replacement'),
  ('WB', 'Wheels align/balance'),
  ('AF', 'Antifreeze added')
)

class Accessory(models.Model):
  name = models.CharField(max_length=50)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('accessories_detail', kwargs={'pk': self.id})


class Car(models.Model):
    make = models.CharField(max_length=100 )
    model = models.CharField(max_length=100 )
    year = models.IntegerField()
    description = models.TextField(max_length=250 )
    # Add the M:M relationship with Accessory
    accessories = models.ManyToManyField(Accessory)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.make

    def get_absolute_url(self):
        return reverse('detail', kwargs={'car_id': self.id})

# Add new Service model
class Service(models.Model):
    date = models.DateField('Service date')
    service = models.CharField(max_length=3, choices=SERVICES, default=SERVICES[0][0])
    # Create a car_id FK
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_service_display()} on {self.date}"

    class Meta:
        ordering = ['-date']

class Photo(models.Model):
    url = models.CharField(max_length=200)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for car_id: {self.car_id} @{self.url}"