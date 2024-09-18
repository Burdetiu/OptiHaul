from django.urls import path
from apps.fleet import views
from main.decorators import user_is_staff_or_manager
from main.views import fleet_index


app_name = 'fleet'

urlpatterns = [
    path('fleet/', fleet_index, name='fleet_index'),

    path('truck-list/', user_is_staff_or_manager(views.TrucksListView.as_view()), name='trucks_list'),
    path('create-truck/', user_is_staff_or_manager(views.CreateTrucksView.as_view()), name='create_truck'),
    path('<int:pk>/update-truck/', user_is_staff_or_manager(views.UpdateTrucksView.as_view()), name='modify-truck'),
    path('<int:pk>/deactivate-truck/', user_is_staff_or_manager(views.deactivate_trucks), name='deactivate-truck'),
    path('<int:pk>/activate-truck/', user_is_staff_or_manager(views.activate_trucks), name='activate-truck'),
    path('<int:pk>/delete-truck/', user_is_staff_or_manager(views.DeleteTrucksView.as_view()), name='delete-truck'),

    path('trailer-list/', user_is_staff_or_manager(views.TrailersListView.as_view()), name='trailers_list'),
    path('create-trailer/', user_is_staff_or_manager(views.CreateTrailersView.as_view()), name='create_trailer'),
    path('<int:pk>/update-trailer/', user_is_staff_or_manager(views.UpdateTrailersView.as_view()), name='modify-trailer'),
    path('<int:pk>/deactivate-trailer/', user_is_staff_or_manager(views.deactivate_trailers), name='deactivate-trailer'),
    path('<int:pk>/activate-trailer/', user_is_staff_or_manager(views.activate_trailers), name='activate-trailer'),
    path('<int:pk>/delete-trailer/', user_is_staff_or_manager(views.DeleteTrailersView.as_view()), name='delete-trailer'),
]