from django.db import models


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
    