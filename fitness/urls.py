from django.urls import path
from fitness.controller.fitness_controller import get_class,create_class,create_slots,book_class,get_bookings

urlpatterns = [
    path('classes', get_class),
    path('create_calss', create_class),
    path('create_slots', create_slots),
    path('book', book_class),
    path('bookings', get_bookings),
]
