# management/views.py

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

