from django.db import models
import datetime

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    role = models.CharField(max_length=25, choices=[('staff', 'staff'), ('admin', 'admin')])
    phone = models.CharField(max_length=25, blank=True)
    hire_date = models.DateField(blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    photo = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        info = '{} {}'.format(self.first_name, self.last_name)
        return info

class Shop(models.Model):
    name = models.CharField(max_length=8)
    
    def __str__(self):
        return self.name
class Shift(models.Model):
    weekday = models.CharField(max_length=20, choices=[('Sunday', 'Sunday'), ('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday')])
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    location = models.ForeignKey(Shop, on_delete=models.CASCADE)
    
    def __str__(self):
        info = '{} at {} from {} to {}'.format(self.weekday, self.location, self.start_time, self.end_time)
        return info
class Schedule(models.Model):
    date = models.DateField(null=True)
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    
    def __str__(self):
        info = '{} at {} from {} to {} on {}'.format(self.employee, self.shift.location, self.shift.start_time, self.shift.end_time, self.date)
        return info


    def shift_dict(self):
        shift_dict = {}
        shift_dict['weekday'] = self.weekday
        shift_dict['start_time'] = self.start_time
        shift_dict['end_time'] = self.end_time
        shift_dict['location'] = self.location
        return shift_dict