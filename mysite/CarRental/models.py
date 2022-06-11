# from unicodedata import name
from django.db import models

#Jakub Zdanowski wypożyczalnia samochodów 
class CarType(models.Model):

    class_A = 'Klasa A'#Miejkie i małe(Fiat 500, Toyota Aygo)
    class_B = 'Klasa B'#Większy w mieście(Renault Clio, Škoda Fabia)
    class_C = 'Klasa C'#Uniwersalne kompakty(Fiat Bravo, Mazda 3)
    class_D = 'Klasa D'#Rodzinna i wygoda(VW Passat,Mazda 6)
    class_E = 'Klasa E'#Dla rodziny i biznesu(Audi A6, BMW serii 5)
    class_F = 'Klasa F'#Luksus i prestiż(BMW seria 7, Audi A8)
    class_S = 'Klasa S'#Sport i prędkość(Porsche 911,Maserati GranTurismo)
    class_H = 'Klasa H'#Powiew powietrza(Mini Cabrio, Porsche 718 Boxster)
    class_J = 'Klasa J'#Na każdą drogę(Range Rover, Porsche Cayenne)
    class_M = 'Klasa M'#Duże i wygodne(Mercedes klasy V,Ford Custom)

    Choice_make = [(class_A, 'Klasa A'),
                    (class_B, 'Klasa B'),
                    (class_C, 'Klasa C'),
                    (class_D, 'Klasa D'),
                    (class_E, 'Klasa E'),
                    (class_F, 'Klasa F'),
                    (class_S, 'Klasa S'),
                    (class_H, 'Klasa H'),
                    (class_J, 'Klasa J'),
                    (class_M, 'Klasa M')]
    
    type = models.CharField(max_length=50, choices=Choice_make)
    

    objects = models.Manager()

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = 'CarType'

class CarFuelType(models.Model):

    Diesel = 'Olej napędowy'
    Gasoline = 'Benzyna'
    Electric = 'Elektryczny'

    Choice_make = [(Diesel, 'Olej napędowy'),
                    (Gasoline, 'Benzyna'),
                    (Electric, 'Elektryczny')]
    
    fueltype = models.ManyToManyField(CarType)
    name = models.CharField(max_length=50, choices=Choice_make)
    
    
    objects = models.Manager()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'FuelType'

class Car(models.Model):

    objects = models.Manager()
    classtype = models.ForeignKey(CarType, on_delete=models.CASCADE)
    fueltype = models.ManyToManyField(CarFuelType)
    production_year = models.IntegerField(default=None)
    brand = models.TextField(max_length=50)
    condition = models.CharField(max_length=50)

    def __str__(self):
        return self.brand
    
    class Meta:
        verbose_name = "Car"