from django.shortcuts import get_object_or_404
from django.views import generic

from .models import Car, CarFuelType, CarType

class IndexView(generic.ListView):
    model = CarType
    template_name = 'carrental/index.html'
    def get_queryset(self):
        return CarType.objects.all()


class DetailView(generic.ListView):
    model = CarFuelType
    template_name = 'carrental/detail.html'
    def get_queryset(self):
        return CarFuelType.objects.all()
    

class ResultsView(generic.DetailView):
    model = Car
    template_name = 'carrental/results.html'
    def get_queryset(self):
        return Car.objects.all()

def vote(request):
    type = get_object_or_404(Car, pk=type)
    