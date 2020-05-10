from django.http import HttpResponse
from django.shortcuts import render

from .models import Pet

def index(requests):
    return HttpResponse('Hello, world!!')

def list_pets(requests):
    
    pets = Pet.objects.all()
    
    return render(requests, 'adopt/list.html',{'pets':pets})
    
def get_pet(requests,pet_id):
    
    pet = Pet.objects.get(id=pet_id)

    return HttpResponse(f'Hello, Ziyang!!! This is {pet.name}.')
# Create your views here.
