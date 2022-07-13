import os
from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee, Shift, Schedule, Shop
import datetime
import calendar

calendar = calendar.TextCalendar(firstweekday=6)

today = datetime.date.today()
day_name = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
idx = (datetime.date.weekday(today) + 1) % 7
day = [datetime.date.today(), day_name[idx]]

sunday = today - datetime.timedelta(idx)

this_week = {
    'today': today,
    'sunday': sunday,
    'monday': sunday + datetime.timedelta(1),
    'tuesday': sunday + datetime.timedelta(2),
    'wednesday': sunday + datetime.timedelta(3),
    'thursday': sunday + datetime.timedelta(4),
    'friday': sunday + datetime.timedelta(5),
    'saturday': sunday + datetime.timedelta(6)

}

def index(request):
    week_sched = {'hello': 'hello'}

    db = Shift
    for day in day_name:
        shifts = db.objects.filter(weekday=day)
        # for n in range(len(shifts)):
        #     week_sched[day] = shifts[n].shift_dict().values()
            # print(shifts[n].shift_dict)
    # print(week_sched)
    # for day in day_name:
    #     day_sched = db.objects.filter(weekday=day)
    #     week_sched[day] = day_sched.shift_dict()
    # for n in week_sched.keys():
    #     week_data = (list(week_sched[n].values()))
        
    # sunday_shifts = list(week_sched['Sunday'].values())
    # for i in sunday_shifts:

    #     print('one more')

    context = {
        'today': day,
        'this_week': this_week,
        # 'sunday_shifts': sunday_shifts,
    #     'monday_shifts': monday_shifts,
    #     'tuesday_shifts': tuesday_shifts,
    #     'wednesday_shifts': wednesday_shifts,
    #     'thursday_shifts': thursday_shifts,
    #     'friday_shifts': friday_shifts,
    #     'saturday_shifts': saturday_shifts
    }
    # print(this_week['sunday'])
    # print(sunday_shifts.location)
    return render(request, 'index.html', context=context)

def emp_sched(emp_name):
    emp_shifts = Shift.objects.filter(id=5)
    print(emp_shifts)
    return HttpResponse(emp_shifts)
