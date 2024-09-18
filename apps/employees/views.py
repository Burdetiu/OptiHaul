from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from main.forms import EmployeeUpdateForm, UserRegistrationForm
from apps.users.models import CustomUser
from apps.users.views import employeeNotifyEmail
import requests


# returns user's ip
def get_user_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


@login_required
def employee_table(request):
    # this is just an ip holder untill deployement, because the get_user_ip returns the port and not the ip
    ip_adress = '188.27.132.100'
    if request.user.is_manager:
        employees = CustomUser.objects.filter(is_employee=True, manager=request.user)
    else:
        employees = CustomUser.objects.filter(is_employee=True)
    for employee in employees:
        response = requests.get(f"https://ipgeolocation.abstractapi.com/v1/?api_key=ac9e7fae88104bccb53a0efc488d8b2d&ip_address={ip_adress}") #ip_address={get_user_ip(request)}
        if response.status_code == 200:
            location_data = response.json()
            employee.latitude = location_data['latitude']
            employee.longitude = location_data['longitude']
        else:
            employee.latitude = "Latitude not found"
            employee.longitude = "Longitude not found"
    context = {'employees': employees}
    return render(request, 'employees/employee_table.html', context)

@login_required
def register_employee(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.is_staff = False
            user.is_manager = False
            user.is_employee = True
            user.status = 'employee'
            user.manager = request.user 
            user.save()

            employeeNotifyEmail(request, user, form.cleaned_data.get('email'))
            
            return redirect('employees:employees_index')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
    else:
        form = UserRegistrationForm()
        
    return render(request, 'employees/register_employee.html', {'form': form})


@login_required
def update_employee(request, pk):
    employee = get_object_or_404(CustomUser, pk=pk, manager=request.user)
    if request.method == 'POST':
        form = EmployeeUpdateForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, f'The employee {employee.first_name} {employee.last_name} has been updated successfully!')
            return redirect('employees:employee_table')
    else:
        form = EmployeeUpdateForm(instance=employee)
    context = {'form': form}
    return render(request, 'employees/edit_employee.html', context)

@login_required
def deactivate_Employees(request, pk):
    CustomUser.objects.filter(id=pk, is_employee=True).update(is_active=False)
    employee = CustomUser.objects.get(id=pk)
    employee.save()
    messages.warning(request, f'the employee {employee.first_name} {employee.last_name} has been deactivated!')
    return redirect('employees:employee_table')

@login_required
def activate_Employees(request, pk):
    CustomUser.objects.filter(id=pk, is_employee=True).update(is_active=True)
    employee = CustomUser.objects.get(id=pk)
    employee.save()
    messages.success(request, f'the employee {employee.first_name} {employee.last_name} has been activated!')
    return redirect('employees:employee_table')

@login_required
def delete_employee(request, pk):
    employee = CustomUser.objects.get(pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('employees:employee_table')
    context = {'employee': employee}
    return render(request, 'employees/on_delete_employee.html', context)