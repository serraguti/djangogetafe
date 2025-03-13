from django.urls import path
from informacion import views

urlpatterns=[
    path('', views.index, name='index'),
    path('pelis/', views.pelis, name='pelis'),
    path('futbol/', views.futbol, name='futbol'),
    path('jugadores/', views.jugadores, name='jugadores'),
    path('colores/', views.colores, name='colores'),
    path('saludo/', views.saludo, name='saludo'),
    path('sumarnumeros/', views.sumarNumeros, name='sumarnumeros'),
    path('collatz/', views.collatz, name='collatz'),
    path('datos/', views.datos, name='datos'),
    path('tabla/', views.tablaMultiplicar, name='tabla'),
    path('insertar/', views.insertarDepartamentos, name='insertar'),    
]