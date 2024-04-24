from django.http import HttpResponse
import mysql.connector
from django.shortcuts import render
from django.http import JsonResponse
from .db_utils import execute_query

def index(request):
    return render(request, 'home.html')

def view_employee(request):
    sql = "SELECT * FROM EMPLOYEE"
    employees = execute_query(sql, fetchall=True)
    return render(request, 'employee.html', {'employees': employees})

def view_facility(request):
    sql = "SELECT * FROM facility"
    facility = execute_query(sql, fetchall=True)
    return render(request, 'facility.html', {'facility': facility})

def view_insurance(request):
    sql = "SELECT * FROM insurance_company"
    insurance_company = execute_query(sql, fetchall=True)
    return render(request, 'insurance.html', {'insurance_company': insurance_company})

def view_patient(request):
    sql = "SELECT * FROM patient"
    patient = execute_query(sql, fetchall=True)
    return render(request, 'patient.html', {'patient': patient})

def view_report(request):
    return render(request, 'report.html')

