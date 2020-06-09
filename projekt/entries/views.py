from django.shortcuts import render, redirect, get_object_or_404
from .models import Iautorsky

def index(request):
    return render(request, 'entries/index.html')

def edit(request,id):
    return render(request, 'entries/edit.html')

def edit_data(request,id):
    obj = Iautorsky.objects.get(id=id)
    jmeno1=request.POST.get("jmeno_e")
    vyzkum1=request.POST.get("vyzkum_e")
    teren1=request.POST.get("teren_e")
    technicky1=request.POST.get("technicky_n")
    kreslil1=request.POST.get("kreslil_n")
    fotografoval1=request.POST.get("fotografoval_n")
    cislo_nove1=request.POST.get("cislo_nove_n")
    obj=Iautorsky(id=id,jmeno=jmeno1,vyzkum=vyzkum1,teren=teren1,technicky=technicky1,kreslil=kreslil1,fotografoval=fotografoval1,cislo_nove=cislo_nove1)
    obj.save()
    return render(request, 'entries/index.html')

def add(request):
    return render(request, 'entries/add.html')
    
def add_data(request):
    jmeno1=request.POST.get("jmeno_n")
    vyzkum1=request.POST.get("vyzkum_n")
    teren1=request.POST.get("teren_n")
    technicky1=request.POST.get("technicky_n")
    kreslil1=request.POST.get("kreslil_n")
    fotografoval1=request.POST.get("fotografoval_n")
    cislo_nove1=request.POST.get("cislo_nove_n")
    obj1=Iautorsky(jmeno=jmeno1,vyzkum=vyzkum1,teren=teren1,technicky=technicky1,kreslil=kreslil1,fotografoval=fotografoval1,cislo_nove=cislo_nove1)
    obj1.save()
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