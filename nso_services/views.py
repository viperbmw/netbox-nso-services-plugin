from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from netbox.views import generic
from dcim.models import Device, DeviceRole
from .models import NSOService, NSOServiceInstance
from .forms import ServiceForm, ServiceInstanceForm, ServiceInstanceAllocationForm
from . import tables, filtersets

# NSO Service Views
class ServiceListView(generic.ObjectListView):
    queryset = NSOService.objects.all()
    table = tables.ServiceTable
    filterset = filtersets.ServiceFilter

class ServiceDetailView(generic.ObjectView):
    queryset = NSOService.objects.all()

class ServiceEditView(generic.ObjectEditView):
    queryset = NSOService.objects.all()
    form = ServiceForm

class ServiceDeleteView(generic.ObjectDeleteView):
    queryset = NSOService.objects.all()

# NSO Service Instance Views
class ServiceInstanceListView(generic.ObjectListView):
    queryset = NSOServiceInstance.objects.all()
    table = tables.ServiceInstanceTable
    filterset = filtersets.ServiceInstanceFilter

class ServiceInstanceDetailView(generic.ObjectView):
    queryset = NSOServiceInstance.objects.all()

class ServiceInstanceEditView(generic.ObjectEditView):
    queryset = NSOServiceInstance.objects.all()
    form = ServiceInstanceForm

class ServiceInstanceDeleteView(generic.ObjectDeleteView):
    queryset = NSOServiceInstance.objects.all()


# Allocation view for assigning instances to devices or device roles
def allocate_instance(request):
    """View to allocate an existing service instance to a device or device role"""
    device_id = request.GET.get('device')
    device_role_id = request.GET.get('device_role')

    if request.method == 'POST':
        form = ServiceInstanceAllocationForm(request.POST)
        if form.is_valid():
            instance = form.cleaned_data['instance']

            if device_id:
                device = get_object_or_404(Device, pk=device_id)
                instance.devices.add(device)
                messages.success(request, f'Allocated "{instance}" to device "{device}"')
                return redirect('dcim:device', pk=device_id)

            elif device_role_id:
                device_role = get_object_or_404(DeviceRole, pk=device_role_id)
                instance.device_roles.add(device_role)
                messages.success(request, f'Allocated "{instance}" to device role "{device_role}"')
                return redirect('dcim:devicerole', pk=device_role_id)
    else:
        form = ServiceInstanceAllocationForm()

    context = {
        'form': form,
        'device_id': device_id,
        'device_role_id': device_role_id,
    }

    return render(request, 'nso_services/allocate_instance.html', context)
