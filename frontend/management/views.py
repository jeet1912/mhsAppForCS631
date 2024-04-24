from django.shortcuts import render
from .db_utils import execute_query
from django.core.paginator import Paginator

def index(request):
    return render(request, 'intro.html')

def view_employee(request):
    sql = "SELECT * FROM EMPLOYEE"
    employees = execute_query(sql, fetchall=True)
    
    paginator = Paginator(employees, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'employee.html', {'employees': page_obj})

def view_facility(request):
    sql = "SELECT * FROM FACILITY"
    facilities = execute_query(sql, fetchall=True)
    return render(request, 'facility.html', {'facilities': facilities})

def view_insurance(request):
    sql = "SELECT * FROM INSURANCE_COMPANY"
    insurance_companies = execute_query(sql, fetchall=True)
    return render(request, 'insurance.html', {'insurance_companies': insurance_companies})

def view_patient(request):
    sql = "SELECT * FROM PATIENT"
    patients = execute_query(sql, fetchall=True)
    return render(request, 'patient.html', {'patients': patients})

def view_report(request):
    # Logic for generating reports
    return render(request, 'report.html')

def view_doctor(request):
    base_sql = """
        SELECT 
            D.*,
            E.FirstName AS EmpFirstName,
            E.MiddleName AS EmpMiddleName,
            E.LastName AS EmpLastName,
            E.Street AS EmpStreet,
            E.City AS EmpCity,
            E.State AS EmpState,
            E.Zip AS EmpZip,
            E.Salary AS EmpSalary,
            E.Date_Hired AS EmpDateHired,
            E.SSN AS SSN,
            E.Fac_ID AS EmpFacilityID
        FROM 
            DOCTOR D
        INNER JOIN 
            EMPLOYEE E ON D.EmployeeID = E.EmployeeID
    """

    page_number = request.GET.get('page')
    
    per_page = 2
    offset = (int(page_number) - 1) * per_page if page_number else 0
    paginate_sql = f"{base_sql} LIMIT {per_page} OFFSET {offset}"
    doctors = execute_query(paginate_sql, fetchall=True)

    count_sql = f"SELECT COUNT(*) AS COUNT FROM ({base_sql}) AS count_query"
    total_doctors_count = execute_query(count_sql, fetchone=True)['COUNT']
    total_pages = (total_doctors_count + per_page - 1) // per_page

    return render(request, 'doctor.html', {'doctors': doctors, 'total_pages': total_pages})


def view_nurse(request):
    sql = "SELECT * FROM NURSE"
    nurses = execute_query(sql, fetchall=True)
    return render(request, 'nurse.html', {'nurses': nurses})

def view_admin_staff(request):
    sql = "SELECT * FROM ADMIN_STAFF"
    admin_staff = execute_query(sql, fetchall=True)
    return render(request, 'admin_staff.html', {'admin_staff': admin_staff})

def view_hcp(request):
    sql = "SELECT * FROM OTHER_HCP"
    other_hcp = execute_query(sql, fetchall=True)
    return render(request, 'hcp.html', {'other_hcp': other_hcp})

def view_employee_assignment(request):
    # Depending on your specific logic for employee assignments, you can fetch data from appropriate tables
    # For example:
    sql = "SELECT * FROM EMPLOYEE_ASSIGNMENT"
    employee_assignments = execute_query(sql, fetchall=True)
    return render(request, 'employee_assignment.html', {'employee_assignments': employee_assignments})
