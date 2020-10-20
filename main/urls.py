from django.urls import path
from .views import main_view, add_file_annul_view, find_our_cars_view, settings_view, add_file_our_cars_view


urlpatterns = [
    path('', main_view, name="main"),
    path('add_file_annul', add_file_annul_view, name="add_file_annul"),
    path('add_file_our_cars', add_file_our_cars_view, name="add_file_our_cars"),
    path('find_our_cars', find_our_cars_view, name="find_our_cars"),
    path('settings', settings_view, name="settings"),

]
