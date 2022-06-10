from django.urls import path
from . import views

urlpatterns = [
    # path('', BookingsView.as_view(), name ='bookings'),
    path('', views.available_tables, name ='bookings'),
    path('addrecord/', views.add_record, name='addrecord'),
]