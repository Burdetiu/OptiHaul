from django.shortcuts import redirect, render
from .decorators import user_is_staff_or_manager
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages


def homepage(request):
    return render(request, 'main/home.html')


@login_required
@user_is_staff_or_manager
def logged_home(request):
    return render(request, 'main/logged_home.html')

@login_required
def logged_employee(request):
    return render(request, 'main/employee_home.html')

@login_required
@user_is_staff_or_manager
def employees_index(request):
    return render(request, 'main/employees_index.html')

@login_required
@user_is_staff_or_manager
def orders_index(request):
    return render(request, 'main/orders_index.html')

@login_required
@user_is_staff_or_manager
def fleet_index(request):
    return render(request, 'main/fleet_index.html')


def contact(request):
    if request.method == 'POST':
        your_name = request.POST['your-name']
        your_surname = request.POST['your-surname']
        your_email = request.POST['your-email']
        your_subject = request.POST['your-subject']
        your_message = request.POST['your-message']
        message = f'From: {your_name} {your_surname} <{your_email}>\n\nSubject: {your_subject}\n\n{your_message}'
        send_mail(
            f'New contact from {your_name} {your_surname}',
            message,
            settings.DEFAULT_FROM_EMAIL,
            [settings.DEFAULT_TO_EMAIL],
            fail_silently=False,
        )
        messages.success(request, f"Thank you <strong>{your_name} {your_surname}</strong> for contacting us! We will get back to you as soon as possible")
        return redirect('home')
    else:
        return render(request, 'main/contact.html')