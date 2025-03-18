from django.urls import path
from television import views

urlpatterns = [
    path('', views.index, name='index'),
    path('series/', views.metodoSeries, name='series'),
    path('personajes/', views.metodoPersonajes, name='personajes'),
]