from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Rider(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    home_address = models.TextField(null=True, blank=True)
    experience = models.IntegerField()
    plate_number = models.CharField(max_length=20, default='ABC5A7')
    online = models.BooleanField(default=True)
    total_completed_rides = models.IntegerField(default=0)
    current_no_of_deliveries = models.IntegerField(default=0)



    def __str__(self, *args, **kwargs):
        return self.user.username



class Ride(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pickup_location = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    price = models.CharField(max_length=100)
    rider = models.ForeignKey(Rider, on_delete=models.PROTECT)

    def __str__(self, *args, **kwargs):
        return self.user.username


class RideHistory(models.Model):
    ride = models.ForeignKey(Ride, on_delete=models.PROTECT, null=True)
    ride_completed = models.BooleanField(default=False)


    def __str__(self, *args, **kwargs):
        return self.ride


