from django.shortcuts import render, redirect, get_object_or_404
from .models import Iautorsky

def index(request):
    return render(request, 'entries/index.html')
def edit(request,id):
    return render(request, 'entries/edit.html') 
def edit_data(request,id):
    jmeno=request.POST.get("jmeno_e")
    vyzkum=request.POST.get("vyzkum_e")
    teren=request.POST.get("teren_e")
    technicky=request.POST.get("technicky_e")
    kreslil=request.POST.get("kreslil_e")
    fotografoval=request.POST.get("fotografoval_e")
    cislo_nove=request.POST.get("cislo_nove_e")
    obj=Iautorsky(jmeno=jmeno,vyzkum=vyzkum,teren=teren,technicky=technicky,kreslil=kreslil,fotografoval=fotografoval,cislo_nove=cislo_nove)
    obj.save()
    return render(request, 'entries/index.html')

def add(request):
    return render(request, 'entries/add.html')
def add_data(request):
    jmeno=request.POST.get("jmeno_n")
    vyzkum=request.POST.get("vyzkum_n")
    teren=request.POST.get("teren_n")
    technicky=request.POST.get("technicky_n")
    kreslil=request.POST.get("kreslil_n")
    fotografoval=request.POST.get("fotografoval_n")
    cislo_nove=request.POST.get("cislo_nove_n")
    obj=Iautorsky(jmeno=jmeno,vyzkum=vyzkum,teren=teren,technicky=technicky,kreslil=kreslil,fotografoval=fotografoval,cislo_nove=cislo_nove)
    obj.save()
    return render(request, 'entries/index.html')

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

def delete_autor(request, id):
    lide = Iautorsky.objects.get(id=id)
    lide.delete()
    return render(request, 'entries/report_smazani.html')

def domu(request):

    return render(request, 'entries/index.html')