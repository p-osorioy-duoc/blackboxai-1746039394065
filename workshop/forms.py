from django import forms
from .models import Vehicle, RepairRecord

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['license_plate', 'brand', 'model', 'year', 'owner_name', 'owner_phone']
        labels = {
            'license_plate': 'Patente',
            'brand': 'Marca',
            'model': 'Modelo',
            'year': 'Año',
            'owner_name': 'Nombre del propietario',
            'owner_phone': 'Teléfono del propietario',
        }
        widgets = {
            'license_plate': forms.TextInput(attrs={'class': 'border rounded p-2 w-full'}),
            'brand': forms.TextInput(attrs={'class': 'border rounded p-2 w-full'}),
            'model': forms.TextInput(attrs={'class': 'border rounded p-2 w-full'}),
            'year': forms.NumberInput(attrs={'class': 'border rounded p-2 w-full'}),
            'owner_name': forms.TextInput(attrs={'class': 'border rounded p-2 w-full'}),
            'owner_phone': forms.TextInput(attrs={'class': 'border rounded p-2 w-full'}),
        }

class RepairRecordForm(forms.ModelForm):
    class Meta:
        model = RepairRecord
        fields = ['vehicle', 'date', 'description', 'cost']
        labels = {
            'vehicle': 'Vehículo',
            'date': 'Fecha de reparación',
            'description': 'Descripción de la reparación',
            'cost': 'Costo',
        }
        widgets = {
            'vehicle': forms.Select(attrs={'class': 'border rounded p-2 w-full'}),
            'date': forms.DateInput(attrs={'class': 'border rounded p-2 w-full', 'type': 'date'}),
            'description': forms.Textarea(attrs={'class': 'border rounded p-2 w-full', 'rows': 4}),
            'cost': forms.NumberInput(attrs={'class': 'border rounded p-2 w-full', 'step': '0.01'}),
        }
