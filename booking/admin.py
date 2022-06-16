from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import AvailableTable, User_Bookings


class AvailableTablesAdmin(admin.ModelAdmin):
    model = AvailableTable
    list_display = [
        "booking_date",
        "time_slot_12",
        "time_slot_14",
        "time_slot_16",
        "time_slot_18",
        "time_slot_20",
        "time_slot_22",
    ]

class User_BookingsAdmin(admin.ModelAdmin):
    model = User_Bookings
    list_display = [
        "booked_name",
        "booked_date",
        "booked_time",
        "booked_tables",
    ]
    
    
admin.site.register(AvailableTable, AvailableTablesAdmin)
admin.site.register(User_Bookings, User_BookingsAdmin)