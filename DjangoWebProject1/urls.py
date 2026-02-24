from django.urls import path
from .views import main_page, second_page, weather_odesa

urlpatterns = [
    path('', main_page, name='main'),
    path('second/', second_page, name='second'),       
    path('weather/', weather_odesa, name='weather'),
]