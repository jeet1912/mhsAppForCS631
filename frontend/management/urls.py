from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('employee/', views.manage_employee, name='manage_employee'),
    path('patient/', views.manage_patient, name='manage_patient'),
    path('report/', views.generate_report, name='generate_report'),
]