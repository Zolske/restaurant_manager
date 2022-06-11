from datetime import datetime, timedelta


# import booking
# from booking.views import available_tables

def weekday_num_to_django(weekday_num=int):
    '''
    converts weekday number Monday = 0 - Sunday = 6 to django weekday numbers Sunday = 1 - Saturday = 7
    '''
    if weekday_num == 6:
        return int(1)
    else:
        return int(weekday_num + 2)
    
def first_date_of_week(year_week=str):
    '''
    parameter: 'yyyy-ww' e.g. '2022-23'\n
    return: 'ddth of MMM' e.g. '06th of Jun'\n
    Takes the year and the week number and returns the date of the first day (Monday) of the week.
    '''
    first_date = datetime.strptime(year_week + '-1', "%Y-%W-%w")
    if first_date.strftime("%d") == '01' or first_date.strftime("%d") == '21' or first_date.strftime("%d") == '31':
        return first_date.strftime("%dst of %b")
    elif first_date.strftime("%d") == '02' or first_date.strftime("%d") == '22':
        return first_date.strftime("%dnd of %b")
    elif first_date.strftime("%d") == '03' or first_date.strftime("%d") == '23':
        return first_date.strftime("%drd of %b")
    else:
        return first_date.strftime("%dth of %b")

def last_date_of_week(year_week=str):
    '''
    parameter: 'yyyy-ww' e.g. '2022-23'\n
    return: 'ddth of MMM' e.g. '12th of Jun'\n
    Takes the year and the week number and returns the date of the last day (Sunday) of the week.
    '''
    last_date = datetime.strptime(year_week + '-0', "%Y-%W-%w")
    if last_date.strftime("%d") == '01' or last_date.strftime("%d") == '21' or last_date.strftime("%d") == '31':
        return last_date.strftime("%dst of %b")
    elif last_date.strftime("%d") == '02' or last_date.strftime("%d") == '22' :
        return last_date.strftime("%dnd of %b")
    elif last_date.strftime("%d") == '03' or last_date.strftime("%d") == '23':
        return last_date.strftime("%drd of %b")
    else:
        return last_date.strftime("%dth of %b")
    
# def update_available_tables_model():
#     for weekday_num in range(7):
#         # function converts weekdays to Django weekdays (1 is Sunday)
#         django_weekday_num = weekday_num_to_django(weekday_num)
#         if weekday_num >= today_day_num:
#             has_data = AvailableTable.objects.filter(booking_date__year=today_year, booking_date__week=today_week, booking_date__week_day=django_weekday_num).values()
#             if not has_data:
#                 accumulate_week_day = today_date + datetime.timedelta(abs(weekday_num - today_day_num))
#                 accumulate_week_day.strftime("%Y-%m-%d")
#                 new_record = AvailableTable(booking_date=accumulate_week_day , time_slot_12=10, time_slot_14=10, time_slot_16=10, time_slot_18=10, time_slot_20=10, time_slot_22=10, )
#                 new_record.save()
#             week_dic[list(week_dic)[weekday_num]] = AvailableTable.objects.filter(booking_date__year=today_year, booking_date__week=today_week, booking_date__week_day=django_weekday_num).values()

def sort_db_oldest_booking(database):
    '''
    Sort database by oldest 'booking_date', returns sorted database as list.
    '''
    available_tables_db = list(database.objects.all().order_by('booking_date').values())
    return available_tables_db

def delete_passed_days(database):
    '''
    Delete database records which have a booking date passed today.
    '''
    # get database, sort by date and save into variable
    available_tables_db = sort_db_oldest_booking(database)
      
    while available_tables_db[0]['booking_date'].strftime("%Y-%m-%d") < datetime.now().strftime("%Y-%m-%d"):
        delete_record = database.objects.get(booking_date=available_tables_db[0]['booking_date'])
        delete_record.delete()
        # update available_tables_db variable with database and sort by booking date
        available_tables_db = sort_db_oldest_booking(database)
        
# def record_today(database, today):
#     '''
#     Create a database entry with todays date if it dose not exist and set time slot value to 10
#     '''
#     available_tables_db = sort_db_oldest_booking(database)
#     # if first record is not today, than add today
#     if available_tables_db[0]['booking_date'].strftime("%Y-%m-%d") != today.strftime("%Y-%m-%d"):
#         new_record = database(booking_date=today, time_slot_12=10, time_slot_14=10, time_slot_16=10, time_slot_18=10, time_slot_20=10, time_slot_22=10 )
#         new_record.save()
        
def add_missing_records(database):
    '''
    ! database needs to be prepared first with function call 'delete_passed_days()' !\n 
    Checks if there are any missing records, missing records are written with default values (booking_date and time slot 10).\n
    There should be a record for every single day from today till 9 weeks later.
    '''
    available_tables_db = sort_db_oldest_booking(database)
    length = len(available_tables_db)
    
    db_list = []
    date_list = []
    
    for record in range(length):
        temp = available_tables_db[record]['booking_date'].strftime("%Y-%m-%d")
        db_list.append(temp)

    for day in range(63):
        temp = (datetime.now() + timedelta(days=day)).strftime("%Y-%m-%d")
        date_list.append(temp)
    
    for day in db_list:
        date_list.remove(day)
    
    for day in date_list:            
        new_record = database(booking_date=day, time_slot_12=10, time_slot_14=10, time_slot_16=10, time_slot_18=10, time_slot_20=10, time_slot_22=10 )
        new_record.save()
 
def write_after_weeks(week_num_after, database):
    '''
    Writes the data from the week after this week into a dictionary which it returns.\n 
    Argument: number of which week after this week e.g. next week is 1, the week after next week is 2 
    '''
    # todays date
    todays_date = datetime.now()
    # this week as number
    this_week_is_num = todays_date.strftime("%W")
    # todays week + how many weeks after
    week_num = int(this_week_is_num) + int(week_num_after)
    
    week_after = {'week_meta':{'week_num':'',
                              'week_start':'',
                              'week_end':''},
                  'Monday':'',
                  'Tuesday':'',
                  'Wednesday':'',
                  'Thursday':'',
                  'Friday':'',
                  'Saturday':'',
                  'Sunday':''}
    
    week_after['week_meta']['week_num'] = week_num
    week_after['week_meta']['week_start'] = first_date_of_week(todays_date.strftime("%Y")+"-"+str(week_num))
    week_after['week_meta']['week_end'] = last_date_of_week(todays_date.strftime("%Y")+"-"+str(week_num))
    # find all booking dates and time slots from this week after
    next_week_booking = list(database.objects.filter(booking_date__week=week_num).order_by('booking_date').values())
    week_after['Monday'] = next_week_booking[0]
    week_after['Tuesday'] = next_week_booking[1]
    week_after['Wednesday'] = next_week_booking[2]
    week_after['Thursday'] = next_week_booking[3]
    week_after['Friday'] = next_week_booking[4]
    week_after['Saturday'] = next_week_booking[5]
    week_after['Sunday'] = next_week_booking[6]
    return week_after 
    
def booking_context_object(database):
    '''
    Create the context dictionary, from the database.\n 
    ! database needs to be prepared first with function call 'delete_passed_days()' and 'add_missing_records()' !\n 
    1. this_week_dic{} : current week, days which have passed are set to false, other days have booking_date and time slot\n 
    2. week_meta_data{} : current week, week_num, week_start, week_end\n 
    3. after_weeks[] : the next 7 weeks, week_num, week_start, week_end, days have booking_date and time slot\n 
    returns return this_week_dic{}, week_meta_data{}, after_weeks[]
    '''
    this_week_dic = {
        'Monday': False,
        'Tuesday': False,
        'Wednesday': False,
        'Thursday': False,
        'Friday': False,
        'Saturday': False,
        'Sunday': False   
    }
    
    this_week_meta = {
        'week_num' : '',
        'week_start' : '',
        'week_end' : ''
        }

    # todays date
    todays_date = datetime.now()
    # this week as number
    this_week_is_num = todays_date.strftime("%W")
    # returns today as day of the week as number 0-6, Monday is 0
    this_week_day_num = todays_date.weekday()
    # find all booking dates from this week
    this_week_booking = list(database.objects.filter(booking_date__week=this_week_is_num).order_by('booking_date').values())
    
    # write days from today to 'this_week_dic' whit there bookings and time slots
    for day in range(7-this_week_day_num):
        this_week_dic[list(this_week_dic)[day + this_week_day_num]] = this_week_booking[day]

    # add this weeks week number, start date and end date
    this_week_meta['week_num'] = this_week_is_num
    this_week_meta['week_start'] = first_date_of_week(todays_date.strftime("%Y-%W"))
    this_week_meta['week_end'] = last_date_of_week(todays_date.strftime("%Y-%W"))
    
    after_weeks = {'week_1':'', 'week_2':'', 'week_3':'', 'week_4':'', 'week_5':'', 'week_6':'', 'week_7':''}
    after_weeks['week_1'] = write_after_weeks(1, database)
    after_weeks['week_2'] = write_after_weeks(2, database)
    after_weeks['week_3'] = write_after_weeks(3, database)
    after_weeks['week_4'] = write_after_weeks(4, database)
    after_weeks['week_5'] = write_after_weeks(5, database)
    after_weeks['week_6'] = write_after_weeks(6, database)
    after_weeks['week_7'] = write_after_weeks(7, database)
    
    # # attach data for the rest of the next 7 weeks

    # for week in range(7):
    #     week_name = 'week_' + str(week)
    #     myVars = vars()
    #     myVars[week_name] = {'week_meta':'',}
        
    #     next_week_num = int(this_week_is_num) + week +1
    #     # week_after = {}
    #     week_meta = {'week_num':'', 'week_start':'', 'week_end':''}
    #     # add this weeks +1 week number, start date and end date
    #     week_meta['week_num'] = next_week_num
    #     week_meta['week_start'] = first_date_of_week(todays_date.strftime("%Y")+"-"+str(next_week_num))
    #     week_meta['week_end'] = last_date_of_week(todays_date.strftime("%Y")+"-"+str(next_week_num))
    #     myVars[week_name] = week_meta
    #     # find all booking dates from this week +1
    #     next_week_booking = list(database.objects.filter(booking_date__week=next_week_num).order_by('booking_date').values())
    #     for day in next_week_booking:
    #         myVars[week_name] = day
    #     after_weeks = myVars[week_name]
        
    return [this_week_dic, this_week_meta, after_weeks]