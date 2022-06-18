from django.db import models

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


class Shift(models.Model):
    date = models.DateField
    start_time = models.TimeField
    end_time = models.TimeField
    location = models.CharField(max_length=10)
    length = models.DurationField
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
