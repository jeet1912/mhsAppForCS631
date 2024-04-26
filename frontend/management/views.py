from django.shortcuts import redirect, render
from .db_utils import execute_query
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse

def index(request):
    return render(request, 'intro.html')

# Employee Management Views
def view_employee(request):
    sql = "SELECT * FROM EMPLOYEE"
    employees = execute_query(sql, fetchall=True)
    
    paginator = Paginator(employees, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'employee/employee.html', {'employees': page_obj})

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

    doctors = execute_query(base_sql, fetchall=True)
    
    paginator = Paginator(doctors, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'employee/doctor.html', {'doctors': page_obj})


def view_nurse(request):
    base_sql = """
        SELECT 
            N.*,
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
            NURSE N
        INNER JOIN 
            EMPLOYEE E ON N.EmployeeID = E.EmployeeID
    """

    nurses = execute_query(base_sql, fetchall=True)
    
    paginator = Paginator(nurses, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'employee/nurse.html', {'nurses': page_obj})

def view_admin_staff(request):
    base_sql = """
        SELECT 
            A.*,
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
            ADMIN_STAFF A
        INNER JOIN 
            EMPLOYEE E ON A.EmployeeID = E.EmployeeID
    """
    admin_staff = execute_query(base_sql, fetchall=True)
    
    paginator = Paginator(admin_staff, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'employee/admin_staff.html', {'admin_staff': page_obj})

def view_hcp(request):
    base_sql = """
        SELECT 
            H.*,
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
            OTHER_HCP H
        INNER JOIN 
            EMPLOYEE E ON H.EmployeeID = E.EmployeeID
    """
    hcps = execute_query(base_sql, fetchall=True)
    
    paginator = Paginator(hcps, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'employee/hcp.html', {'other_hcp': page_obj})

def add_employee(request):
    if request.method == 'POST':
        ssn = request.POST.get('ssn')
        first_name = request.POST.get('first_name')
        middle_name = request.POST.get('middle_name', '')
        last_name = request.POST.get('last_name')
        street = request.POST.get('street')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip')
        salary = request.POST.get('salary')
        date_hired = request.POST.get('date_hired')
        job_class = request.POST.get('job_class')
        facility_id = request.POST.get('facility_id')

        # Inserting into EMPLOYEE table
        employee_sql = """
        INSERT INTO EMPLOYEE (SSN, FirstName, MiddleName, LastName, Street, City, State, Zip, Salary, Date_Hired, Job_Class, Fac_ID)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        employee_params = (ssn, first_name, middle_name, last_name, street, city, state, zip_code, salary, date_hired, job_class, facility_id)
        execute_query(employee_sql, params=employee_params)

        employee_sql = """SELECT EmployeeID FROM EMPLOYEE WHERE SSN = %s"""
        employee_id = execute_query(employee_sql, [ssn], fetchone=True)
        # Inserting into specific table based on job class
        if job_class == 'Doctor':
            speciality = request.POST.get('speciality')
            board_certification_date = request.POST.get('board_certification_date')
            doctor_sql = """
            INSERT INTO DOCTOR (EmployeeID, Speciality, Board_Certification_Date)
            VALUES (%s, %s, %s)
            """
            doctor_params = (employee_id["EmployeeID"],speciality, board_certification_date)
            execute_query(doctor_sql, params=doctor_params)
        elif job_class == 'Nurse':
            certification = request.POST.get('certification')
            nurse_sql = """
            INSERT INTO NURSE (EmployeeID, Certification)
            VALUES %s, %s)
            """
            nurse_params = (employee_id["EmployeeID"], certification)
            execute_query(nurse_sql, params=nurse_params)
        elif job_class == 'HCP':
            practice_area = request.POST.get('practice_area')
            hcp_sql = """
            INSERT INTO OTHER_HCP (EmployeeID, Practice_Area)
            VALUES (%s, %s)
            """
            hcp_params = (employee_id["EmployeeID"],practice_area)
            execute_query(hcp_sql, params=hcp_params)
        elif job_class == 'Admin':
            job_title = request.POST.get('job_title')
            admin_sql = """
            INSERT INTO ADMIN_STAFF (EmployeeID, Job_Title)
            VALUES (%s, %s)
            """
            admin_params = (employee_id["EmployeeID"],job_title)
            execute_query(admin_sql, params=admin_params)

        return redirect('add_employee')

    # Fetching facility IDs for dropdown
    facility_sql = "SELECT Facility_ID FROM FACILITY"
    facilities = execute_query(facility_sql, fetchall=True)
    return render(request, 'employee/add_employee.html', {'facilities': facilities})

def edit_employee(request):
    if request.method == 'POST':
        # Retrieve form data
        employee_id = request.POST.get('employee_id')
        ssn = request.POST.get('ssn')
        first_name = request.POST.get('first_name')
        middle_name = request.POST.get('middle_name', '')
        last_name = request.POST.get('last_name')
        street = request.POST.get('street')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip')
        salary = request.POST.get('salary')
        date_hired = request.POST.get('date_hired')
        job_class = request.POST.get('job_class')
        facility_id = request.POST.get('facility_id')

        # Update EMPLOYEE table
        employee_sql = """
        UPDATE EMPLOYEE 
        SET SSN = %s, FirstName = %s, MiddleName = %s, LastName = %s, Street = %s, City = %s, State = %s, Zip = %s, Salary = %s, Date_Hired = %s, Job_Class = %s, Fac_ID = %s
        WHERE EmployeeID = %s
        """
        employee_params = (ssn, first_name, middle_name, last_name, street, city, state, zip_code, salary, date_hired, job_class, facility_id, employee_id)
        execute_query(employee_sql, params=employee_params)

        # Update specific table based on job class
        if job_class == 'Doctor':
            speciality = request.POST.get('speciality')
            board_certification_date = request.POST.get('board_certification_date')
            doctor_sql = """
            UPDATE DOCTOR 
            SET Speciality = %s, Board_Certification_Date = %s
            WHERE EmployeeID = %s
            """
            doctor_params = (speciality, board_certification_date, employee_id)
            execute_query(doctor_sql, params=doctor_params)
        elif job_class == 'Nurse':
            certification = request.POST.get('certification')
            nurse_sql = """
            UPDATE NURSE 
            SET Certification = %s
            WHERE EmployeeID = %s
            """
            nurse_params = (certification, employee_id)
            execute_query(nurse_sql, params=nurse_params)
        elif job_class == 'HCP':
            practice_area = request.POST.get('practice_area')
            hcp_sql = """
            UPDATE OTHER_HCP 
            SET Practice_Area = %s
            WHERE EmployeeID = %s
            """
            hcp_params = (practice_area, employee_id)
            execute_query(hcp_sql, params=hcp_params)
        elif job_class == 'Admin':
            job_title = request.POST.get('job_title')
            admin_sql = """
            UPDATE ADMIN_STAFF 
            SET Job_Title = %s
            WHERE EmployeeID = %s
            """
            admin_params = (job_title, employee_id)
            execute_query(admin_sql, params=admin_params)

        return redirect('edit_employee')
    
    sql = "SELECT * FROM EMPLOYEE"
    employees = execute_query(sql, fetchall=True)
    employee_id = request.GET.get('employeeIdDropdown')
    if employee_id:
        emp = get_employee_details(employee_id)
        facility_sql = "SELECT Facility_ID FROM FACILITY"
        facilities = execute_query(facility_sql, fetchall=True)
        print(emp)
        return render(request, 'employee/edit_employee.html',{'employee_details': emp, 'employees': employees, 'facilities': facilities})
    return render(request, 'employee/edit_employee.html',{'employees': employees})

def get_employee_details(employee_id):
        employee_query = """
        SELECT * FROM EMPLOYEE WHERE EmployeeID = %s
        """
        employee_data = execute_query(employee_query, [employee_id], fetchone=True)

        if employee_data:
            # Determine the job class of the employee
            job_class = employee_data['Job_Class']

            # Fetch additional details based on job class
            if job_class == 'Doctor':
                details_query = """
                SELECT Speciality, Board_Certification_Date FROM DOCTOR WHERE EmployeeID = %s
                """
            elif job_class == 'Nurse':
                details_query = """
                SELECT Certification FROM NURSE WHERE EmployeeID = %s
                """
            elif job_class == 'HCP':
                details_query = """
                SELECT Practice_Area FROM OTHER_HCP WHERE EmployeeID = %s
                """
            elif job_class == 'Admin':
                details_query = """
                SELECT Job_Title FROM ADMIN_STAFF WHERE EmployeeID = %s
                """

            additional_details = execute_query(details_query, [employee_id], fetchone=True)

            # Merge employee data with additional details
            employee_data.update(additional_details)

            return employee_data

def view_facility(request):
    sql = "SELECT * FROM FACILITY"
    facilities = execute_query(sql, fetchall=True)
    paginator = Paginator(facilities, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'facility/facility.html', {'facilities': page_obj})

def view_ob(request):
    sql = """
    SELECT f.*, ob.Office_Count 
    FROM FACILITY f 
    JOIN OFFICE_BUILDING ob ON f.Facility_ID = ob.Facility_ID
    """
    facilities = execute_query(sql, fetchall=True)
    paginator = Paginator(facilities, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'facility/office_building.html', {'facilities': page_obj})


def view_ops(request):
    sql = """
    SELECT f.*, ops.Room_Count, ops.Procedure_Code, ops.Description
    FROM FACILITY f 
    JOIN OUTPATIENT_SURGERY ops ON f.Facility_ID = ops.Facility_ID
    """
    facilities = execute_query(sql, fetchall=True)
    paginator = Paginator(facilities, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'facility/ops.html', {'facilities': page_obj})

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
