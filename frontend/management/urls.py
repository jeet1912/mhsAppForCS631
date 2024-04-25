from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('facility/', views.view_facility, name='view_facility'),
    path('insurance/', views.view_insurance, name='view_insurance'),
    path('patient/', views.view_patient, name='view_patient'),
    path('report/', views.view_report, name='view_report'),
    path('emp/doctor/', views.view_doctor, name='view_doctor'),
    path('emp/nurse/', views.view_nurse, name='view_nurse'),
    path('emp/admin_staff/', views.view_admin_staff, name='view_admin_staff'),
    path('emp/hcp/', views.view_hcp, name='view_hcp'),
    path('emp/add_employee/', views.add_employee, name='add_employee'),
    path('emp/edit_employee/', views.edit_employee, name='edit_employee'),
    path('emp/', views.view_employee, name='view_employee'),
]
