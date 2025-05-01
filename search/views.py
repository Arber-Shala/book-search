from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# request -> response

def main_menu(request):
    return HttpResponse("Main Menu")

def say_hello(request):
    return render(request, 'hello.html', {"name": "Arber"})
