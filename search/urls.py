from django.urls import path
from . import views

from django.urls import URLPattern, URLResolver


urlpatterns:list[URLResolver|URLPattern] = [
    path('', views.main_menu),
    path('search/', views.say_hello),
]




