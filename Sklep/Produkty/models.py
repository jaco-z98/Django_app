from django.db import models

class Producent(models.Model):
    
    nazwa = models.CharField(max_length=60)                                                       #max 60 znaków
    opis = models.TextField(blank=True)                                                           #opis nie jest obowiązkowy

    def __str__(self):
        return self.nazwa

    class Meta:
        verbose_name = "Producent"
        verbose_name_plural = "Producenci"

class Kategoria(models.Model):
    
    nazwa = models.CharField(max_length=30)                                                      #max 30 znaków

    def __str__(self):
        return self.nazwa
    
    class Meta:
        verbose_name = "Kategoria"
        verbose_name_plural = "Kategorie"

class Produkty(models.Model):
    
    nazwa = models.CharField(max_length=100)                                                     #max 100 znaków
    opis = models.TextField(blank=True)                                                          #opis nie jest obowiązkowy
    cena = models.DecimalField(max_digits=12, decimal_places=2)                                  #12 znaków, dwa miejsca po przecinku  
    producent = models.ForeignKey(Producent, on_delete=models.CASCADE, null=True)                #klucz obcy dla Producenta
    kategoria = models.ForeignKey(Kategoria, on_delete=models.CASCADE, null=True, blank=True)    #klucz obcy dla Kategorii

    def __str__(self):
        return self.nazwa

    class Meta:
        verbose_name = "Produkt"
        verbose_name_plural = "Produkty"