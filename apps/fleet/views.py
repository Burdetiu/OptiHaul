from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.fleet.models import Trucks, Trailers
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from main.forms import TrailersForm, TrucksForm



# Trucks
class TrucksListView(LoginRequiredMixin,ListView):
    model = Trucks
    template_name = 'fleet/trucks/trucks_list.html'

    def get_queryset(self):
        user = self.request.user
        if user.is_manager:
            queryset = Trucks.objects.filter(created_by=user)
        else:
            queryset = Trucks.objects.all()
        return queryset
    
    
# Trailers
class TrailersListView(LoginRequiredMixin,ListView):
    model = Trailers
    template_name = 'fleet/trailers/trailers_list.html'

    def get_queryset(self):
        user = self.request.user
        if user.is_manager:
            queryset = Trailers.objects.filter(created_by=user)
        else:
            queryset = Trailers.objects.all()
        return queryset


# Trucks
class CreateTrucksView(LoginRequiredMixin, CreateView):
    template_name = 'fleet/trucks/trucks_form.html'
    form_class = TrucksForm
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        messages.success(self.request, f'the truck {self.object.registration_plate} has been successfully created!')
        return reverse('fleet:trucks_list')


# Trailers   
class CreateTrailersView(LoginRequiredMixin, CreateView):
    template_name = 'fleet/trailers/trailers_form.html'
    form_class = TrailersForm

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        messages.success(self.request, f'the trailer {self.object.registration_plate} has been successfully created!')
        return reverse('fleet:trailers_list')


# Trucks
class UpdateTrucksView(LoginRequiredMixin, UpdateView):
    template_name = 'fleet/trucks/trucks_form.html'
    form_class = TrucksForm

    def get_success_url(self):
        messages.success(self.request, f'the truck {self.object.registration_plate} has been successfully updated!')
        return reverse('fleet:trucks_list')


# Trailers    
class UpdateTrailersView(LoginRequiredMixin, UpdateView):
    template_name = 'fleet/trailers/trailers_form.html'
    form_class = TrailersForm

    def get_success_url(self):
        messages.success(self.request, f'the trailer {self.object.registration_plate} has been successfully updated!')
        return reverse('fleet:trailers_list')

# Trucks
@login_required
def deactivate_trucks(request, pk):
    Trucks.objects.filter(id=pk).update(status=False)
    truck = Trucks.objects.get(id=pk)
    truck.save()
    messages.warning(request, f'the truck {truck.registration_plate} is now non-operational!')
    return redirect('fleet:trucks_list')

# Trailers
@login_required
def deactivate_trailers(request, pk):
    Trailers.objects.filter(id=pk).update(status=False)
    trailer = Trailers.objects.get(id=pk)
    trailer.save()
    messages.warning(request, f'the trailer {trailer.registration_plate} is now non-operational!')
    return redirect('fleet:trailers_list')

# Trucks
@login_required
def activate_trucks(request, pk):
    Trucks.objects.filter(id=pk).update(status=True)
    truck = Trucks.objects.get(id=pk)
    truck.save()
    messages.success(request, f'the truck {truck.registration_plate} is now operational!')
    return redirect('fleet:trucks_list')

# Trailers
@login_required
def activate_trailers(request, pk):
    Trailers.objects.filter(id=pk).update(status=True)
    trailer = Trailers.objects.get(id=pk)
    trailer.save()
    messages.success(request, f'the trailer {trailer.registration_plate} is now operational!')
    return redirect('fleet:trailers_list')

# Trucks
class DeleteTrucksView(LoginRequiredMixin, DeleteView):
    model = Trucks
    template_name = 'fleet/trucks/on_delete_truck.html'

    def get_success_url(self):
        messages.warning(self.request, f'the truck {self.object.registration_plate} has been permanently deleted!')
        return reverse('fleet:trucks_list')

# Trailers
class DeleteTrailersView(LoginRequiredMixin, DeleteView):
    model = Trailers
    template_name = 'fleet/trailers/on_delete_trailer.html'

    def get_success_url(self):
        messages.warning(self.request, f'the trailer {self.object.registration_plate} has been permanently deleted!')
        return reverse('fleet:trailers_list')