from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('reports/1', views.revenue_report_by_facility, name='view_report1'),
    path('reports/2', views.appointments_by_date_and_physician, name='view_report2'),
    path('reports/3', views.appointments_by_time_period_and_facility, name='view_report3'),
    path('reports/4', views.best_revenue_days_for_month, name='view_report4'),
    path('reports/5', views.average_daily_revenue_by_insurance_company, name='view_report5'),
    #Facility Views
    path('facility/', views.view_facility, name='view_facility'),
    path('facility/ob', views.view_ob, name='view_ob'),
    path('facility/ops', views.view_ops, name='view_ops'),
    path('facility/add', views.create_facility, name='create_facility'),
    path('facility/edit', views.edit_facility, name='edit_facility'),
    #Employee Views
    path('emp/doctor/', views.view_doctor, name='view_doctor'),
    path('emp/nurse/', views.view_nurse, name='view_nurse'),
    path('emp/admin_staff/', views.view_admin_staff, name='view_admin_staff'),
    path('emp/hcp/', views.view_hcp, name='view_hcp'),
    path('emp/add_employee/', views.add_employee, name='add_employee'),
    path('emp/edit_employee/', views.edit_employee, name='edit_employee'),
    path('emp/', views.view_employee, name='view_employee'),
    #Patient Views
    path('patient/add_patient/', views.add_patient, name='add_patient'),
    path('patient/', views.view_patient, name='view_patient'),
    path('patient/edit_patient/', views.edit_patient, name='edit_patient'),
    path('patient/make_appointment', views.make_appointment, name='make_appointment'),
    path('patient/update_appointment', views.update_appointment, name='update_appointment'),
    path('patient/daily_inv', views.daily_inv, name='daily_inv'),
    path('patient/all_appointment/', views.view_appointment, name='view_appointment'),
    #Insurance Views
    path('insurance/', views.view_insurance, name='view_insurance'),
    path('insurance/add_insurance', views.add_insurance, name='add_insurance'),
    path('insurance/edit_insurance', views.edit_insurance, name='edit_insurance'),
]
