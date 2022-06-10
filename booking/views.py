from itertools import accumulate
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
import datetime
from .models import AvailableTable
from local_module.local_functions import weekday_num_to_django

# todays date
today_date = 0
# todays day as a number, Sunday = 0
today_day_num = 0
# todays week starting from Monday
today_week = 0
# todays year
today_year = 0

    
def available_tables(request):
    # todays date
    today_date = datetime.datetime.now()
    # returns today as day of the week as number, Monday is 0
    today_day_num = today_date.weekday()
    # %W returns this Weeks' number of the year, Monday as the first day of week, 00-53
    today_week = today_date.strftime("%W")
    # %Y returns this Year, full version e.g. 2018
    today_year = today_date.strftime("%Y")
    # dictionary which represents the weeks bookings
    week_dic = {
        'Monday': False,
        'Tuesday': False,
        'Wednesday': False,
        'Thursday': False,
        'Friday': False,
        'Saturday': False,
        'Sunday': False        
    }

    
    for weekday_num in range(7):
        # function converts weekdays to Django weekdays (1 is Sunday)
        django_weekday_num = weekday_num_to_django(weekday_num)
        if weekday_num >= today_day_num:
            has_data = AvailableTable.objects.filter(booking_date__year=today_year, booking_date__week=today_week, booking_date__week_day=django_weekday_num).values()
            if not has_data:
                accumulate_week_day = today_date + datetime.timedelta(abs(weekday_num - today_day_num))
                accumulate_week_day.strftime("%Y-%m-%d")
                new_record = AvailableTable(booking_date=accumulate_week_day , time_slot_12=10, time_slot_14=10, time_slot_16=10, time_slot_18=10, time_slot_20=10, time_slot_22=10, )
                new_record.save()
            week_dic[list(week_dic)[weekday_num]] = AvailableTable.objects.filter(booking_date__year=today_year, booking_date__week=today_week, booking_date__week_day=django_weekday_num).values()
            
    template = loader.get_template('bookings.html')
    context = {
    'today' : today_date,
    'week' :  week_dic,
    }
    return HttpResponse(template.render(context, request))

def add_record(request):
    new_booking_date = request.POST['new_booking_date']
    new_time_slot = request.POST['time_slot']
    new_num_tables = request.POST['num_tables']
    
    new_record = AvailableTable(booking_date=new_booking_date, time_slot_12=new_num_tables )
    new_record.save()
    
    time_slot_list = ['time_slot_12', 'time_slot_14', 'time_slot_16', 'time_slot_18', 'time_slot_20', 'time_slot_22']
    # for slot in time_slot_list:
    #     if slot == new_time_slot:
    #          new_record = AvailableTable(booking_date=new_booking_date, slot=new_num_tables )
    #          new_record.save()
             
    return HttpResponseRedirect(reverse('bookings'))

