from tkinter import CASCADE
from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL


max_table = 10
# Create your models here.
class AvailableTable(models.Model):
    booking_date = models.DateField(primary_key=True)
    time_slot_12 = models.PositiveSmallIntegerField(default=max_table)
    time_slot_14 = models.PositiveSmallIntegerField(default=max_table)
    time_slot_16 = models.PositiveSmallIntegerField(default=max_table)
    time_slot_18 = models.PositiveSmallIntegerField(default=max_table)
    time_slot_20 = models.PositiveSmallIntegerField(default=max_table)
    time_slot_22 = models.PositiveSmallIntegerField(default=max_table)

    class Meta:
        ordering = ['booking_date']

    def __str__(self):
        return "%s (%s,%s,%s,%s,%s,%s)" % (self.booking_date, self.time_slot_12,
                                           self.time_slot_14, self.time_slot_16,
                                           self.time_slot_18, self.time_slot_20,
                                           self.time_slot_22)
    

class User_Bookings(models.Model):  
    booked_name = models.ForeignKey(User, on_delete=models.CASCADE)
    booked_date = models.DateField()
    booked_time = models.CharField(max_length=6)
    booked_tables = models.PositiveSmallIntegerField()
    
    def __str__(self):
        return "%s (%s,%s,%s)" % (self.booked_name, self.booked_date,
                                  self.booked_time, self.booked_tables)    
