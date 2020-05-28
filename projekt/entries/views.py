from django.shortcuts import render, redirect
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

def delete(request):
    entries = Iautorsky.objects.all()

    context = {'entries' : entries}

    return render(request, 'entries/delete.html', context)


def delete_autor(request):




    
    return render(request, 'entries/report_smazani.html')

def domu(request):

    return render(request, 'entries/index.html')