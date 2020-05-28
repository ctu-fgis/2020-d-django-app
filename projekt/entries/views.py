from django.shortcuts import render
from django.shortcuts import redirect
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
    results=Iautorsky.objects.all()
    return render(request, 'entries/delete.html',{"Iautorsky":results})

def delete_autor(request, pk):
    obj = Iautorsky.objects.get(id=pk)
    if request.method == 'GET':
        obj.delete()
        return redirect('/')
    return render(request, 'entries/report_smazani.html')

def domu(request):

    return render(request, 'entries/index.html')