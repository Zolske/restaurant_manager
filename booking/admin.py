from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import AvailableTable


class AvailableTablesAdmin(UserAdmin):
    model = AvailableTable
    list_display = [
        "booking_date",
        "time_slot_12",
    ]
    fieldsets = UserAdmin.fieldsets
    add_fieldsets = UserAdmin.add_fieldsets


admin.site.register(AvailableTable)