from django.urls import path
from departamentos import views

urlpatterns = [
    path('', views.index, name='index')
]