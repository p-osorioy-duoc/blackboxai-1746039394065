from django import forms
from .models import Vehicle, RepairRecord

class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ['name', 'phone']
        labels = {
            'name': 'Nombre del propietario',
            'phone': 'Teléfono del propietario',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'border rounded p-2 w-full'}),
            'phone': forms.TextInput(attrs={'class': 'border rounded p-2 w-full'}),
        }

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['license_plate', 'brand', 'model', 'year', 'owner']
        labels = {
            'license_plate': 'Patente',
            'brand': 'Marca',
            'model': 'Modelo',
            'year': 'Año',
            'owner': 'Propietario',
        }
        widgets = {
            'license_plate': forms.TextInput(attrs={'class': 'border rounded p-2 w-full'}),
            'brand': forms.TextInput(attrs={'class': 'border rounded p-2 w-full'}),
            'model': forms.TextInput(attrs={'class': 'border rounded p-2 w-full'}),
            'year': forms.NumberInput(attrs={'class': 'border rounded p-2 w-full'}),
            'owner': forms.Select(attrs={'class': 'border rounded p-2 w-full'}),
        }

class RepairRecordForm(forms.ModelForm):
    class Meta:
        model = RepairRecord
        fields = ['vehicle', 'date', 'description', 'cost', 'next_maintenance_date']
        labels = {
            'vehicle': 'Vehículo',
            'date': 'Fecha de reparación',
            'description': 'Descripción de la reparación',
            'cost': 'Costo',
            'next_maintenance_date': 'Fecha próxima mantención',
        }
        widgets = {
            'vehicle': forms.Select(attrs={'class': 'border rounded p-2 w-full'}),
            'date': forms.DateInput(attrs={'class': 'border rounded p-2 w-full', 'type': 'date'}),
            'description': forms.Textarea(attrs={'class': 'border rounded p-2 w-full', 'rows': 4}),
            'cost': forms.NumberInput(attrs={'class': 'border rounded p-2 w-full', 'step': '0.01'}),
            'next_maintenance_date': forms.DateInput(attrs={'class': 'border rounded p-2 w-full', 'type': 'date'}),
        }
