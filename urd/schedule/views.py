from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Shift
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
    shifts = Shift.objects.all()
    for shift in shifts:
        print(shifts.date)
        print(shifts.employee) 
    context = {
        'today': day[0],
        'this_week': this_week
    }
    print(this_week['monday'])
    return render(request, 'index.html', context=context)

def emp_sched(emp_name):
    emp_shifts = Shift.objects.filter(id=5)
    print(emp_shifts)
    return HttpResponse(emp_shifts)
