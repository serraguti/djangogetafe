from django.urls import path
from aplicacion import views

urlpatterns = [
    path('', views.index, name='index')
]
#http://127.0.0.1:8000/magia/
#http://127.0.0.1:8000/magia/futbol/