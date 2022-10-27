
from django.shortcuts import get_object_or_404, render
from .models import Car, CarType
# class IndexView(generic.ListView):
#     model = CarType
#     template_name = 'carrental/index.html'
#     def get_queryset(self):
#         return CarType.objects.all()


# class DetailView(generic.ListView):
#     model = CarFuelType
#     template_name = 'carrental/detail.html'
#     def get_queryset(self):
#         return CarFuelType.objects.all()
    

# class ResultsView(generic.DetailView):
#     model = Car
#     template_name = 'carrental/results.html'
#     def get_queryset(self):
#         return Car.objects.all()

def vote(request):
    type = get_object_or_404(Car, pk=type)

def index(request):
    wszystkie = Car.objects.all()
    kategorie = CarType.objects.all()
    dane = {'wszystkie' : wszystkie,
            'kategorie' : kategorie}
    return render(request,'index.html', dane)

def detail(request, id):
    kategoria_user = CarType.objects.get(pk=id)
    kategoria_car = Car.objects.filter(kategoria = kategoria_car)
    kategorie = CarType.objects.all()
    dane = {'kategoria_user' : kategoria_user,
            'kategoria_car' : kategoria_car,
            'kategorie' : kategorie}
    return render(request, 'detail.html', dane)

def result(request, id):
    Car = Car.objects.get(pk=id)
    kategorie = CarType.objects.all()
    dane = {'Car' : Car,
            'kategorie' : kategorie}
    return render(request,'result.html', dane)