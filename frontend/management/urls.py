from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('employee/', views.view_employee, name='view_employee'),
    path('facility/', views.view_facility, name='view_facility'),
    path('insurance/', views.view_insurance, name='view_insurance'),
]