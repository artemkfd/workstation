from django.urls import path
from . import views



urlpatterns = [
    path('', views.search_view, name="search"),
    path('car_info/<int:car_id>', views.car_info, name='car_info'),
]