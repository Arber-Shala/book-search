from django.shortcuts import render
from django.http import HttpResponse

from .models import Book
from django.db.models import Q
# Create your views here.
# request -> response

def main_menu(request):
    return render(request, 'main_menu.html', {"name": "Arber"})

def search_results(request):
    model = Book

    # books = Book.objects.all()
    # queryset = Book.objects.filter(name__icontains='The Karamazov Brothers') # only get objectswith name = 'The Karamazov Brothers'
    #filter = Book.objects.filter(Q(name__icontains="The Karamazov Brothers") | Q(name__icontains="Crime and Punishment")) # filter for either OR books
    
    query = request.GET.get("q")

    object_list = Book.objects.filter(Q(name__icontains=query))

    num_objects = Book.objects.all().count() # get total number of objects in the queryset
    num_filtered_objects = object_list.count() # get number of objects filtered for in search
    
    # by default, search returns all objects, so if the search returns all objects we actually have no matches
    if(num_filtered_objects == num_objects):
        object_list = None

    return render(request, 'search_results.html', {"model": object_list})
