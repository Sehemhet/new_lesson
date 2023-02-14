from django.http import HttpResponse
from django.shortcuts import render


def HomeDef(request):
    return render(request, 'home/home.html')
# Create your views here.
