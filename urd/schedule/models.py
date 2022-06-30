from django.db import models
import datetime

class User(models.Model):
    first_name = models.CharField(max_length=100, default=' ')
    last_name = models.CharField(max_length=100, default=' ')
    email = models.EmailField(blank=True, null=True)
    role = models.CharField(max_length=25)
    phone = models.CharField(max_length=25, blank=True)
    hire_date = models.DateField(null=True)
    birthday = models.DateField(blank=True, null=True)
    notes = models.TextField(blank=True)
    photo = models.FilePathField(blank=True)


    def __str__(self):
        name = self.first_name + '  ' + self.last_name
        return name


class Schedule(models.Model):
    day = models.CharField(max_length=20)
    date = models.DateField(null=True)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    location = models.CharField(max_length=20, choices=[('O1', 'O1'), ('O2', 'O2'), ('O3', 'O3')])
    length = models.DurationField(blank=True, null=True)
    employee = models.ForeignKey(User, on_delete=models.CASCADE)

class Shift(models.Model):
    weekday = models.CharField(max_length=20, choices=[('Sunday', 'Sunday'), ('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday')])
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    location = models.CharField(max_length=20, choices=[('O1', 'O1'), ('O2', 'O2'), ('O3', 'O3')])

    def __str__(self):
        shift = '{}, {}, {}, {}'.format(self.weekday, self.start_time, self.end_time, self.location)
        return shift

    def shift_dict(self):
        shift_dict = {}
        shift_dict['weekday'] = self.weekday
        shift_dict['start_time'] = self.start_time
        shift_dict['end_time'] = self.end_time
        shift_dict['location'] = self.location
        return shift_dict