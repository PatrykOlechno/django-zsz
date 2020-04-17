from django.urls import path
from staff.views import StaffView

urlpatterns = [
    path('', StaffView.as_view())
]
