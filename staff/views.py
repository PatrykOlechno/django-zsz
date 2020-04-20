from django.shortcuts import render
from django.views import generic
from staff.models import Member

app_name = 'staff'

class StaffView(generic.ListView):
    template_name = 'staff.html'
    model = Member
