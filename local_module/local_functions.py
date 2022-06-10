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
    first_date = datetime.datetime.strptime(year_week + '-1', "%Y-%W-%w")
    if first_date.strftime("%d") == 1:
        return first_date.strftime("%dst of %b")
    elif first_date.strftime("%d") == 2:
        return first_date.strftime("%dnd of %b")
    elif first_date.strftime("%d") == 3:
        return first_date.strftime("%drd of %b")
    else:
        return first_date.strftime("%dth of %b")

def last_date_of_week(year_week=str):
    '''
    parameter: 'yyyy-ww' e.g. '2022-23'\n
    return: 'ddth of MMM' e.g. '12th of Jun'\n
    Takes the year and the week number and returns the date of the last day (Sunday) of the week.
    '''
    last_date = datetime.datetime.strptime(year_week + '-0', "%Y-%W-%w")
    if last_date.strftime("%d") == 1:
        return last_date.strftime("%dst of %b")
    elif last_date.strftime("%d") == 2:
        return last_date.strftime("%dnd of %b")
    elif last_date.strftime("%d") == 3:
        return last_date.strftime("%drd of %b")
    else:
        return last_date.strftime("%dth of %b")
    
def update_available_tables_model():
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