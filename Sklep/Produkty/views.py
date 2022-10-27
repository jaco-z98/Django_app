from django.shortcuts import render
from .models import Kategoria, Produkty

def index(request):
    wszystkie = Produkty.objects.all()
    kategorie = Kategoria.objects.all()
#     kat = Produkty.objects.filter(kategoria=4)
#     kat_name = Kategoria.objects.get(id=1)  
#     null = Produkty.objects.filter(kategoria__isnull=False)
    producent = Produkty.objects.filter(producent=2)                            
    dane = {'wszystkie' : wszystkie,
            'kategorie' : kategorie,
            'producent' : producent}
    return render(request,'index.html', dane)

def kategoria(request, id):
    kategoria_user = Kategoria.objects.get(pk=id)
    kategoria_produkt = Produkty.objects.filter(kategoria = kategoria_user)
    kategorie = Kategoria.objects.all()
    dane = {'kategoria_user' : kategoria_user,
            'kategoria_produkt' : kategoria_produkt,
            'kategorie' : kategorie}
    return render(request, 'detail.html', dane)

def produkt(request, id):
    produkt_user = Produkty.objects.get(pk=id)
    kategorie = Kategoria.objects.all()
    dane = {'produkt_user' : produkt_user,
            'kategorie' : kategorie}
    return render(request,'result.html', dane)
