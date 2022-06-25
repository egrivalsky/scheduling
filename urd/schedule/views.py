from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Shift
import datetime
import calendar

calendar = calendar.TextCalendar(firstweekday=6)

def index(request):
    # month = calendar.formatmonth(2022, 6, w=0, l=0)
    month = calendar.monthdatescalendar(2022, 6)
    today = datetime.date.today()
    day_name = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    day = day_name[datetime.date.weekday(today)]
    context = {
        'today': day
    }
    print(day_name[datetime.date.weekday(today)])
    return render(request, 'index.html', context=context)

def emp_sched(emp_name):
    emp_shifts = Shift.objects.filter(id=5)
    print(emp_shifts)
    return HttpResponse(emp_shifts)
