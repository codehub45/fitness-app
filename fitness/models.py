from django.db import models
from django.utils.timezone import now

# Create your models here.

class Classes(models.Model):
    class_name = models.CharField(max_length=100)
    instructor = models.CharField(max_length=100)


class Slots(models.Model):
    slots = models.IntegerField()
    start_timings = models.TimeField(default=now,null=True)
    end_timings = models.TimeField(default=now,null=True)
    classes = models.ForeignKey(Classes, on_delete=models.CASCADE,null=True)


class Bookings(models.Model):
    class_id = models.ForeignKey(Classes, on_delete=models.CASCADE,null=True)
    client_name = models.CharField(max_length=100)
    client_email = models.CharField(max_length=100)
    date_time = models.DateField()
    slots = models.ForeignKey(Slots, on_delete=models.CASCADE,null=True)
