from django.shortcuts import render
from .models import Iautorsky

def index(request):
    entries = Iautorsky.objects.all()
    
    context = {'entries' : entries}

    return render(request, 'entries/index.html', context)

def add(request):
    return render(request, 'entries/add.html')