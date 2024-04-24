from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('employee/', views.view_employee, name='view_employee'),
    path('facility/', views.view_facility, name='view_facility'),
    path('insurance/', views.view_insurance, name='view_insurance'),
    path('patient/', views.view_patient, name='view_patient'),
    path('report/', views.view_report, name='view_report'),
    path('doctor/', views.view_doctor, name='view_doctor'),
    path('nurse/', views.view_nurse, name='view_nurse'),
    path('admin_staff/', views.view_admin_staff, name='view_admin_staff'),
    path('hcp/', views.view_hcp, name='view_hcp'),
    path('employee_assignment/', views.view_employee_assignment, name='view_employee_assignment'),
]
