from django.urls import path
from apps.orders import views
from main.decorators import user_is_staff_or_manager
from main.views import orders_index

app_name = 'orders'

urlpatterns = [
    path('orders/', orders_index, name='orders_index'),
    
    path('orders-list/', user_is_staff_or_manager(views.OrdersListView.as_view()), name='orders_list'),
    path('create/', user_is_staff_or_manager(views.CreateOrdersView.as_view()), name='create_order'),
    path('<int:pk>/update/', user_is_staff_or_manager(views.UpdateOrdersView.as_view()), name='modify'),
    path('<int:pk>/deactivate/', user_is_staff_or_manager(views.deactivate_orders), name='deactivate'),
    path('<int:pk>/activate/', user_is_staff_or_manager(views.activate_orders), name='activate'),
    path('<int:pk>/delete/', user_is_staff_or_manager(views.DeleteOrdersView.as_view()), name='delete'),
]
