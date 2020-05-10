from django.http import HttpResponse

from .models import Pet

def index(requests):
    return HttpResponse('Hello, world!!')

def list_pets(requests):
    response = '<ul>'  # unordered list

    pets = Pet.objects.all()

    for pet in pets:
        response += f'<li><a href="/adopt/{pet.id}">{pet.name}</a></li>'
    
    response += '</ul>'

    return HttpResponse(response)

def get_pet(requests,pet_id):
    
    pet = Pet.objects.get(id=pet_id)

    


    return HttpResponse(f'Hello, Ziyang!!! This is {pet.name}.')
# Create your views here.
