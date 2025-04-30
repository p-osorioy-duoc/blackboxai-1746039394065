from django.shortcuts import render, redirect, get_object_or_404
from .models import Vehicle, RepairRecord
from .forms import VehicleForm, RepairRecordForm

def vehicle_list(request):
    vehicles = Vehicle.objects.all().order_by('-created_at')
    return render(request, 'workshop/vehicle_list.html', {'vehicles': vehicles})

def vehicle_create(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vehicle_list')
    else:
        form = VehicleForm()
    return render(request, 'workshop/vehicle_form.html', {'form': form})

def repair_create(request):
    if request.method == 'POST':
        form = RepairRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vehicle_list')
    else:
        form = RepairRecordForm()
    return render(request, 'workshop/repair_form.html', {'form': form})

def vehicle_detail(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    repairs = vehicle.repairs.all().order_by('-date')
    return render(request, 'workshop/vehicle_detail.html', {'vehicle': vehicle, 'repairs': repairs})
