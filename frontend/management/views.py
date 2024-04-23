# management/views.py

from django.http import HttpResponse
import mysql.connector
from django.shortcuts import render

def db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="mhs"
    )

def index(request):
    return HttpResponse("Welcome to the MHS Management System.")

def manage_employee(request):
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM EMPLOYEE")
    employees = cursor.fetchall()
    cursor.close()
    conn.close()
    return render(request, 'employee.html', {'employees': employees})

def manage_patient(request):
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM PATIENT")
    patients = cursor.fetchall()
    cursor.close()
    conn.close()
    return render(request, 'management/patient.html', {'patients': patients})

def generate_report(request):
    # Placeholder function for reports
    return HttpResponse("Reports Page")
