from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sched', views.emp_sched, name='emp_sched')
]