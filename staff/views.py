from django.shortcuts import render
from django.views import generic

app_name = 'staff'

class StaffView(generic.ListView):
    template_name = 'staff.html'
