from django.urls import path
from . import views



urlpatterns = [
    path('', views.main_view, name="main"),
    path('add_file_annul', views.add_file_annul_view, name="add_file_annul"),
    path('add_file_our_cars', views.add_file_our_cars_view, name="add_file_our_cars"),
    path('add_file_reestr_ba', views.add_file_reestr_ba_view, name="add_file_reestr_ba"),
    path('find_our_cars', views.find_our_cars_view, name="find_our_cars"),
    path('settings', views.settings_view, name="settings"),
    path('propusk_table', views.propusk_table_view, name="propusk_table"),

]
