from django.urls import path
from . import views

urlpatterns = [
    path('', views.vehicle_list, name='vehicle_list'),
    path('vehiculo/nuevo/', views.vehicle_create, name='vehicle_create'),
    path('reparacion/nueva/', views.repair_create, name='repair_create'),
    path('vehiculo/<int:pk>/', views.vehicle_detail, name='vehicle_detail'),
]
