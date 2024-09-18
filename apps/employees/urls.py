from django.urls import path
from apps.employees import views
from main.decorators import user_is_staff_or_manager
from main.views import employees_index

app_name = 'employees'

urlpatterns = [
    path('employees/', employees_index, name='employees_index'),

    path('table/', user_is_staff_or_manager(views.employee_table), name='employee_table'),
    path('register_employee/', user_is_staff_or_manager(views.register_employee), name='register_employee'),
    path('<int:pk>/update/', user_is_staff_or_manager(views.update_employee), name='modify'),
    path('<int:pk>/deactivate/', user_is_staff_or_manager(views.deactivate_Employees), name='deactivate'),
    path('<int:pk>/activate/', user_is_staff_or_manager(views.activate_Employees), name='activate'),
    path('<int:pk>/delete/', user_is_staff_or_manager(views.delete_employee), name='delete'),
]