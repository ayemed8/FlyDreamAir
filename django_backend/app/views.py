from asyncore import read
from django.shortcuts import render
from app.utils.paths import get_international_csv_path
from app.utils.util import read_csv

def home(request):

    return render(request, 'home.html')

def create_account(request):
    return render(request, 'create_account.html')

def login(request):
    return render(request, 'login.html')

def choose_flight(request):
    return render(request, 'departing_flights.html')

def fill_passenger_info(request):
    return render(request, 'passenger_info.html')

def fill_extra_service(request):
    return render(request, 'extra_services.html')

def choose_seat(request):
    return render(request, 'seat_selection.html')

def make_payment(request):
    return render(request, 'payment_detail.html')

def show_booking(request):
    return render(request, 'my_booking.html')