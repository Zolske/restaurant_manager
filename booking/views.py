from itertools import accumulate
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
import datetime
from .models import AvailableTable, User_Bookings
from local_module.local_functions import weekday_num_to_django, delete_passed_days, add_missing_records, booking_context_object
   
def available_tables(request):
    delete_passed_days(AvailableTable)
    add_missing_records(AvailableTable)
    this_week_dic, this_week_meta, after_weeks = booking_context_object(AvailableTable)
    user_now = request.user
    # has_bookings, user_booking_list = check_user_bookings(user_now, User_Bookings)
    
    user_booking_list = User_Bookings.objects.filter(booked_name=user_now).values()
    has_bookings = len(user_booking_list)
            
    template = loader.get_template('booking/bookings.html')
    context = {
    'user_logged_in' : False,
    'this_week_dic' : this_week_dic,
    'this_week_meta' : this_week_meta,
    'after_weeks' : after_weeks,
    'current_user' : user_now,
    'has_bookings' : has_bookings,
    'user_booking_list' : user_booking_list,
    }
    # is set to true only if the user is logged in
    if request.user.is_authenticated:
        context['user_logged_in'] = True
        
    return HttpResponse(template.render(context, request))

def add_record(request):
    new_booking_date = request.POST['new_booking_date']
    new_time_slot = request.POST['time_slot']
    new_num_tables = request.POST['num_tables']
    booking_record = list(AvailableTable.objects.filter(booking_date=new_booking_date).values())

    for record in booking_record[0]:
        if new_time_slot == record:
            booking_record[0][record] = int(booking_record[0][record]) - int(new_num_tables)
            for key, value in booking_record[0].items() :
                if key == 'booking_date':
                    value_booking = value
                if key == 'time_slot_12':
                    value_12 = value
                if key == 'time_slot_14':
                    value_14 = value
                if key == 'time_slot_16':
                    value_16 = value
                if key == 'time_slot_18':
                    value_18 = value
                if key == 'time_slot_20':
                    value_20 = value
                if key == 'time_slot_22':
                    value_22 = value
                   
            new_record = AvailableTable(booking_date=value_booking, time_slot_12=value_12, time_slot_14=value_14, time_slot_16=value_16, time_slot_18=value_18, time_slot_20=value_20, time_slot_22=value_22 )
            new_record.save()
    
    print(type(value_booking))
    
    user_now = request.user
    booking_time = new_time_slot[-2:]
    booking_time += ':00'       
    table_num = int(new_num_tables)
    new_booking_record = User_Bookings(booked_name=user_now, booked_date=value_booking, booked_time=booking_time, booked_tables=table_num)
    new_booking_record.save()
    
    return HttpResponseRedirect(reverse('bookings'))