from django.shortcuts import render
from django.http  import Http404
from .models import  Pet
def home(request):
    pets = Pet.objects.all()
    return render(request,'home.html',{'data':pets,})

def pet_details(request, pet_id):
    try:
        pet = Pet.objects.get(id=pet_id)
        print(pet)
    except:
        raise Http404('Pet Not Found !')
    return render(request, 'pet_details.html',{'data':pet,})