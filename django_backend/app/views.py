from django.shortcuts import render
from app.utils.paths import get_meal_menu_csv_path
from app.utils.util import read_csv, get_country_info

def home(request):
    countries : list

    country_city_code = get_country_info()
    return render(request, 'home.html', {'country_city_code': country_city_code})

def login(request):
    return render(request, 'login.html')

def choose_flight(request):
    return render(request, 'departing_flights.html')

def fill_passenger_info(request):
    return render(request, 'passenger_info.html')

def fill_extra_service(request):
    foods : list 
    drinks : list
    
    path = get_meal_menu_csv_path()

    foods = read_csv(csv_name=path, column_name='Food')
    drinks = read_csv(csv_name=path, column_name='Drink')
    
    return render(request, 'extra_services.html', {"foods": foods, "drinks": drinks})

def choose_seat(request):
    return render(request, 'seat_selection.html')

def make_payment(request):
    return render(request, 'payment_detail.html')

def show_booking(request):
    return render(request, 'my_booking.html')