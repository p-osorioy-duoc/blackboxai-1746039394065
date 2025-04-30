from django.urls import path
from . import views

urlpatterns = [
    path('', views.vehicle_list, name='vehicle_list'),
    path('vehiculo/nuevo/', views.vehicle_create, name='vehicle_create'),
    path('reparacion/nueva/', views.repair_create, name='repair_create'),
    path('vehiculo/<int:pk>/', views.vehicle_detail, name='vehicle_detail'),
    path('mantenciones/futuras/', views.maintenance_calendar, name='maintenance_calendar'),
    path('propietarios/', views.owner_list, name='owner_list'),
    path('propietarios/nuevo/', views.owner_create, name='owner_create'),
]
