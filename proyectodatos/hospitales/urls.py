from django.urls import path
from hospitales import views

urlpatterns = [
    path('', views.index, name='index'),
    path('departamentos/', views.departamentosBBDD, name='departamentos'),
    path('hospitales/', views.hospitalesBBDD, name='hospitales'),
    path('insertardept/', views.insertarDepartamento, name='insertardept'),
    path('deletedepartamento/', views.eliminarDepartamento, name='deletedept'),
    path('updatedepartamento/', views.updateDepartamento, name='updatedept'),
    path('detallesdepartamento/', views.detallesDepartamento, name='detallesdept'),
    path('empleadosdepartamento/', views.empleadosDepartamento, name='empdept')
]