from django.shortcuts import render

# Create your views here.
from .models import place, travellers


def demo(request):
    obj = place.objects.all()
    obj1 = travellers.objects.all()
    return render(request, "index.html", {'result': obj, 'output': obj1})

# def demo1(request):
#     obj1 = travellers.objects.all()
#     return render(request, "index.html", {'result': obj1})
