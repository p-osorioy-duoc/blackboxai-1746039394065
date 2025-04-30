from django.shortcuts import render, redirect, get_object_or_404
from .models import Vehicle, RepairRecord, Owner
from .forms import VehicleForm, RepairRecordForm, OwnerForm
from django.utils import timezone
from django.db.models import Q

def vehicle_list(request):
    query = request.GET.get('q', '')
    vehicles = Vehicle.objects.all().order_by('-created_at')
    if query:
        vehicles = vehicles.filter(
            Q(license_plate__icontains=query) |
            Q(brand__icontains=query) |
            Q(model__icontains=query) |
            Q(owner__name__icontains=query)
        )
    return render(request, 'workshop/vehicle_list.html', {'vehicles': vehicles, 'query': query})

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

def maintenance_calendar(request):
    today = timezone.now().date()
    future_maintenances = RepairRecord.objects.filter(next_maintenance_date__gte=today).order_by('next_maintenance_date')
    return render(request, 'workshop/maintenance_calendar.html', {'future_maintenances': future_maintenances})

def owner_list(request):
    owners = Owner.objects.all().order_by('name')
    return render(request, 'workshop/owner_list.html', {'owners': owners})

def owner_create(request):
    if request.method == 'POST':
        form = OwnerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('owner_list')
    else:
        form = OwnerForm()
    return render(request, 'workshop/owner_form.html', {'form': form})
