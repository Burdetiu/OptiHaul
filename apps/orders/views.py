from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from main.forms import OrdersForm
from apps.orders.models import Orders
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages




class OrdersListView(LoginRequiredMixin, ListView):
    model = Orders
    template_name = 'orders/orders_list.html'
    
    def get_queryset(self):
        user = self.request.user
        if user.is_manager:
            queryset = Orders.objects.filter(created_by=user)
        else:
            queryset = Orders.objects.all()
        return queryset

        


class CreateOrdersView(LoginRequiredMixin, CreateView):
    template_name = 'orders/orders_form.html'
    form_class = OrdersForm

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        messages.success(self.request, 'the order has been successfully created!')
        return reverse('orders:orders_list')


class UpdateOrdersView(LoginRequiredMixin, UpdateView):
    model = Orders
    template_name = 'orders/orders_form.html'
    form_class = OrdersForm

    def get_success_url(self):
        messages.success(self.request, 'the order has been successfully edited!')
        return reverse('orders:orders_list')


@login_required
def deactivate_orders(request, pk):
    Orders.objects.filter(id=pk).update(status=False)
    messages.success(request, 'the order is completed!')
    return redirect('orders:orders_list')


@login_required
def activate_orders(request, pk):
    Orders.objects.filter(id=pk).update(status=True)
    messages.warning(request,  'the order is uncompleted!')
    return redirect('orders:orders_list')


class DeleteOrdersView(LoginRequiredMixin, DeleteView):
    model = Orders
    template_name = 'orders/on_delete_orders.html'

    def get_success_url(self):
        messages.error(self.request, 'the order has been successfully deleted!')
        return reverse('orders:orders_list')
