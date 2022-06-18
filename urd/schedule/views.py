from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Shift




def index(request):
    return HttpResponse("Hello, world. You're at the SCHEDULING index.")

def emp_sched(emp_name):
    emp_shifts = Shift.objects.filter(id=5)
    print(emp_shifts)
    return HttpResponse(emp_shifts)
