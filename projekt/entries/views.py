from django.shortcuts import render
from .models import Iautorsky

def index(request):
    return render(request, 'entries/index.html')

def add(request):
    return render(request, 'entries/add.html')

def data(request):
    entries = Iautorsky.objects.all()
    
    context = {'entries' : entries}

    return render(request, 'entries/data.html', context)

def login(request):
    return render(request, 'entries/login.html')