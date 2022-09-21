from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('create-account/', views.create_account, name='create-account'),
    path('login/', views.login, name='login'),
    path('flights/', views.choose_flight, name='available-flights'),
    path('my-info/', views.fill_passenger_info, name='my-info'),
    path('flight-extra-services/', views.fill_extra_service, name='extra-services'),
    path('flight-seats/', views.choose_seat, name='available-seats'),
    path('payment/', views.make_payment, name='my-payment'),
    path('flight-tickets/', views.show_booking, name='my-tickets'),
]