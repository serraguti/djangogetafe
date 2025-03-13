from django.urls import path
from hospitales import views

urlpatterns = [
    path('', views.index, name='index')
]