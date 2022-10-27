from django.urls import path

from . import views

app_name = 'CarRental'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/results/', views.result, name='results'),
    path('<int:type>/vote/', views.vote, name='vote'),
]