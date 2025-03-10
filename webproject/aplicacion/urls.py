from django.urls import path
from aplicacion import views

urlpatterns = [
    path('', views.index, name='index'),
    path('viernes/', views.metodoViernes, name='viernes'),
    path('peli/', views.paginaPelicula, name='peli')
]
#http://127.0.0.1:8000/magia/
#http://127.0.0.1:8000/magia/futbol/