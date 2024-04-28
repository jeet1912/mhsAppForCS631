from django.shortcuts import redirect, render
from .db_utils import execute_query
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
import datetime

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
        print("****EMPLOYEES*** ",emp)
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

def edit_facility(request):
    if request.method == 'POST':
        # Retrieve form data
        facility_id = request.POST.get('facility_id')
        street = request.POST.get('street')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip')
        facility_type = request.POST.get('facility_type')
        max_size = request.POST.get('size')
        facility_type = facility_type.replace("_", " ")
        # Update FACILITY table
        facility_sql = """
        UPDATE FACILITY
        SET Street = %s, City = %s, State = %s, Zip = %s, Facility_Type = %s, MaxSize = %s
        WHERE Facility_ID = %s
        """
        facility_params = (street, city, state, zip_code, facility_type, max_size, facility_id)
        execute_query(facility_sql, params=facility_params)

        # Update specific facility type details
        if facility_type == 'Office':
            office_count = request.POST.get('office_count')
            office_sql = """
            UPDATE OFFICE_BUILDING
            SET Office_Count = %s
            WHERE Facility_ID = %s
            """
            office_params = (office_count, facility_id)
            execute_query(office_sql, params=office_params)
        elif facility_type == 'OP Surgery':
            room_count = request.POST.get('room_count')
            procedure_code = request.POST.get('procedure_code')
            description = request.POST.get('description')
            ops_sql = """
            UPDATE OUTPATIENT_SURGERY
            SET Room_Count = %s, Procedure_Code = %s, Description = %s
            WHERE Facility_ID = %s
            """
            ops_params = (room_count, procedure_code, description, facility_id)
            execute_query(ops_sql, params=ops_params)

        return redirect('edit_facility')

    # Retrieve all facilities to display in a dropdown for editing
    sql = "SELECT * FROM FACILITY"
    facilities = execute_query(sql, fetchall=True)
    facility_id = request.GET.get('facilityDropdown')
    if facility_id:
        facility_details = get_facility_details(facility_id)
        return render(request, 'facility/edit_facility.html', {'facility_details': facility_details, 'facilities': facilities})
    
    return render(request, 'facility/edit_facility.html', {'facilities': facilities})

def get_facility_details(facility_id):
    # First, get the facility type
    type_sql = "SELECT Facility_Type FROM FACILITY WHERE Facility_ID = %s"
    facility_type = execute_query(type_sql, params=(facility_id,), fetchone=True)

    if facility_type['Facility_Type'] == 'OP Surgery':
        # Query details for outpatient surgery
        sql = """
        SELECT f.*, ops.Room_Count, ops.Procedure_Code, ops.Description
        FROM FACILITY f
        LEFT JOIN OUTPATIENT_SURGERY ops ON f.Facility_ID = ops.Facility_ID
        WHERE f.Facility_ID = %s
        """
    else:
        # Query details for office building
        sql = """
        SELECT f.*, ob.Office_Count
        FROM FACILITY f
        LEFT JOIN OFFICE_BUILDING ob ON f.Facility_ID = ob.Facility_ID
        WHERE f.Facility_ID = %s
        """

    facility_details = execute_query(sql, params=(facility_id,), fetchone=True)
    return facility_details

def create_facility(request):
    if request.method == 'POST':
        street = request.POST.get('street')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip')
        size = request.POST.get('size')
        facility_type = request.POST.get('facility_type')
        facility_type = facility_type.replace("_", " ")
        sql_insert_facility = """
        INSERT INTO FACILITY (Street, City, State, Zip, MaxSize, Facility_Type)
        VALUES (%s, %s, %s, %s, %s,  %s)
        """
        facility_id = execute_query(sql_insert_facility, (street, city, state, zip_code, size, facility_type), insert_new = True)

        if facility_type == 'Office':
            office_count = request.POST.get('office_count')
            sql_insert_office = """
            INSERT INTO OFFICE_BUILDING (Facility_ID, Office_Count)
            VALUES (%s, %s)
            """
            execute_query(sql_insert_office, (facility_id, office_count))

        elif facility_type == 'OP Surgery':
            room_count = request.POST.get('room_count')
            procedure_code = request.POST.get('procedure_code')
            description = request.POST.get('description', '')
            sql_insert_surgery = """
            INSERT INTO OUTPATIENT_SURGERY (Facility_ID, Room_Count, Procedure_Code, Description)
            VALUES (%s, %s, %s, %s)
            """
            execute_query(sql_insert_surgery, (facility_id, room_count, procedure_code, description))

        # Redirect to a new URL after POST
        return redirect('create_facility') 
    return render(request, 'facility/add_facility.html')

def view_insurance(request):
    sql = "SELECT * FROM INSURANCE_COMPANY"
    insurance_companies = execute_query(sql, fetchall=True)
    paginator = Paginator(insurance_companies, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'insurance/view_insurance.html', {'insurance_companies': page_obj})

def add_insurance(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        street = request.POST.get('street')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip')
        sql_add_insurance = """
        INSERT INTO INSURANCE_COMPANY (Name, Street, City, State, Zip)
        VALUES (%s, %s, %s, %s, %s)
        """
        execute_query(sql_add_insurance, (name, street, city, state, zip_code))
        return redirect('add_insurance')
    return render(request, 'insurance/add_insurance.html')

def edit_insurance(request):
    if request.method == 'POST':
        insurance_id = request.POST.get('insurance_id')
        name = request.POST.get('name')
        street = request.POST.get('street')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip')
        sql_edit_insurance = """
        UPDATE INSURANCE_COMPANY
        SET Name = %s, Street = %s, City = %s, State = %s, Zip = %s
        WHERE InsuranceComp_ID = %s
        """
        param = (name, street, city, state, zip_code, insurance_id)
        y = execute_query(sql_edit_insurance, params=param)
        print('views.py EDIT INSURANCE ',y)
        return redirect('edit_insurance')
    sql = "SELECT * FROM INSURANCE_COMPANY"
    insurance_companies = execute_query(sql, fetchall=True)
    #print("VIEWs.py FETCHED? ",len(insurance_companies))
    insurance_id = request.GET.get('insuranceDropdown')
    #print("VIEWs.py INSURANCE ID::",insurance_id)
    if insurance_id:
        insurance_details = get_insurance_details(insurance_id)
        return render(request, 'insurance/edit_insurance.html', {'insurance_details': insurance_details, 'insurance_companies': insurance_companies})
    return render(request, 'insurance/edit_insurance.html', {'insurance_companies': insurance_companies})

def get_insurance_details(insurance_id):
    #print("VIEWS.py COMPANY :: ",insurance_id)
    sql = """
    SELECT * FROM INSURANCE_COMPANY WHERE InsuranceComp_ID = %s
    """
    #print("SQL is ",sql)
    insurance_details = execute_query(sql, (insurance_id), fetchone=True)
    #print('Insurance Details ',insurance_details)
    return insurance_details

def view_patient(request):
    sql = "SELECT * FROM PATIENT"
    patients = execute_query(sql, fetchall=True)
    paginator = Paginator(patients, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'patient/patient.html', {'patients': page_obj})

def add_patient(request):
    doctors_sql = """
                    SELECT d.EmployeeID, e.FirstName, e.LastName
                    FROM DOCTOR d
                    JOIN EMPLOYEE e ON d.EmployeeID = e.EmployeeID 
                """
    doctors = execute_query(doctors_sql, fetchall=True)

    insurances_sql = "SELECT InsuranceComp_ID, Name FROM INSURANCE_COMPANY"
    insurances = execute_query(insurances_sql, fetchall=True)

    if request.method == 'POST':
        first_name = request.POST['first_name']
        middle_name = request.POST.get('middle_name', '')
        last_name = request.POST['last_name']
        street = request.POST['street']
        city = request.POST['city']
        state = request.POST['state']
        zip_code = request.POST['zip']
        first_visit_date = request.POST['first_visit_date']
        doctor_id = request.POST['doctor_id']
        incomp_id = request.POST['incomp_id']
        
        insert_patient_sql = """
        INSERT INTO PATIENT (FirstName, MiddleName, LastName, Street, City, State, Zip, First_Visit_Date, Doctor_ID, InComp_ID)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        patient_params = (first_name, middle_name, last_name, street, city, state, zip_code, first_visit_date, doctor_id, incomp_id)
        execute_query(insert_patient_sql, patient_params)
        return redirect('add_patient')
    return render(request, 'patient/add_patient.html', {'doctors': doctors, 'insurances': insurances})

def make_appointment(request):
    if request.method == 'POST':
        patient_id = request.POST['patient_id']
        doctor_id = request.POST['doctor_id']
        appointment_date = request.POST['appointment_date']
        appointment_time = request.POST['appointment_time']
        facility_id = request.POST['facility_id']
        datetime = f"{appointment_date} {appointment_time}:00"
        cost = '0.00'
        invD_ID = None
        insert_appointment_sql = """
        INSERT INTO MAKES_APPOINTMENT (Pat_ID, Doc_ID, Date_Time, Fac_ID, InD_ID)
        VALUES (%s, %s, %s, %s, %s)
        """
        appointment_params = (patient_id, doctor_id, datetime, facility_id, invD_ID)
        execute_query(insert_appointment_sql, appointment_params)
        return redirect('make_appointment')
    patients_sql = "SELECT Patient_ID FROM PATIENT"
    patients = execute_query(patients_sql, fetchall=True)
    doctors_sql = "SELECT EmployeeID FROM DOCTOR"
    doctors = execute_query(doctors_sql, fetchall=True)
    facilities_sql = "SELECT Facility_ID FROM FACILITY"
    facilities = execute_query(facilities_sql, fetchall=True)
    return render(request, 'patient/make_appointment.html', {'patients': patients, 'doctors': doctors, 'facilities': facilities})


def update_appointment(request):
    if request.method == 'POST':
            cost = request.POST['cost']
            patient_id = request.POST['patient_id']
            doctor_id = request.POST['doctor_id']
            facility_id = request.POST['facility_id']
            appointment_datetime = request.POST['appointment_datetime']
            #formatted_date_time = appointment_datetime.strftime('%Y-%m-%dT%H:%M')
            date = appointment_datetime.split(' ')[0]
            
            print('VIEWS.py  COST ',cost)
            print('VIEWS.py  PATIENT ID ',patient_id)
            print('VIEWS.py  DOCTOR ID ',doctor_id)
            print('VIEWS.py  APPOINTMENT DATE TIME ',appointment_datetime)
            print('VIEWS.py  FACILITY ID ',facility_id)
            insuranceComp_sql = """
            SELECT InComp_ID FROM PATIENT WHERE Patient_ID = %s
            """
            incomp_id = execute_query(insuranceComp_sql, [patient_id], fetchone=True)
            incomp_id = incomp_id['InComp_ID']
            print("VIEWS.py  INSURANCE ID ",incomp_id)

            print("VIEWS.py  DATE ",date)
            date = datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M')
            date2 = date.strftime('%Y-%m-%d')
            print('VIEWS.py  DATE for INV ',date2)

            getInvoiceID = """
            SELECT Inv_ID FROM INVOICE
            WHERE InComp_ID = %s and InvDate = %s
            """
            invoice_id = execute_query(getInvoiceID, (incomp_id, date2), fetchone=True)
            print('Does invoice exist?', invoice_id)
            if invoice_id is None:
                insert_invoice_sql = """
                INSERT INTO INVOICE (InvDate, InComp_ID)
                VALUES (%s, %s)
                """
                latest_invoice_id = execute_query(insert_invoice_sql, (date2, incomp_id), insert_new=True)
                print('New invoice ID:', latest_invoice_id)
                invoice_id = latest_invoice_id
            
            print("VIEWS.py  INVOICE ID :", invoice_id)

            insert_invoice_details_sql = """
            INSERT INTO INVOICE_DETAIL (Inv_ID, Cost)
            VALUES (%s, %s)
            """
            ind_id = execute_query(insert_invoice_details_sql, (invoice_id, cost), insert_new=True)
            print("VIEWS.py  INVOICE DETAILS ID : ", ind_id)

            date3 = date.strftime('%Y-%m-%d %H:%M:%S')
            print('VIEWS.py  DATE for Appointment ',date3)
            
            update_appointment_sql = """
            UPDATE MAKES_APPOINTMENT 
            SET InD_ID = %s
            WHERE Pat_ID = %s AND Doc_ID = %s AND Date_Time = %s AND Fac_ID = %s
            """
            appointment_params = (ind_id, patient_id, doctor_id, date3, facility_id)
            execute_query(update_appointment_sql, appointment_params)
            return redirect('update_appointment')
        
    #appointments = execute_query("SELECT * FROM MAKES_APPOINTMENT", fetchall=True)
    #date = appointments.Date_Time.datesplit(' ')[0]
    #time = appointments.Date_Time.split(' ')[1]
    patients_sql = "SELECT Patient_ID FROM PATIENT"
    patients = execute_query(patients_sql, fetchall=True)
    doctors_sql = "SELECT EmployeeID FROM DOCTOR"
    doctors = execute_query(doctors_sql, fetchall=True)
    facilities_sql = "SELECT Facility_ID FROM FACILITY"
    facilities = execute_query(facilities_sql, fetchall=True)
    
    patient_id = request.GET.get('patient_id')
    doctor_id = request.GET.get('doctor_id')
    facility_id = request.GET.get('facility_id')
    appointment_date = request.GET.get('appointment_date')
    appointment_time = request.GET.get('appointment_time')
    #print('Appointment Date:', appointment_date)
    #print('Appointment Time:', appointment_time)
    appointment_datetime = f"{appointment_date} {appointment_time}:00"
    print('Appointment DateTime:', appointment_datetime)
    if patient_id and doctor_id and facility_id and appointment_date and appointment_time:
        appointment_sql = """
            SELECT * FROM MAKES_APPOINTMENT
            WHERE Pat_ID = %s AND Doc_ID = %s AND Date_Time = %s AND Fac_ID = %s
        """
        appointment = execute_query(appointment_sql, (patient_id, doctor_id, appointment_datetime, facility_id), fetchone=True)
        print('Query Result:', appointment)
        if (appointment and (appointment['InD_ID'] is None)):
            return render(request, 'patient/update_appointment.html', {'patients': patients, 'doctors': doctors, 'facilities': facilities, 'appointment': appointment})
    return render(request, 'patient/update_appointment.html', {'patients': patients, 'doctors': doctors, 'facilities': facilities})


def view_report(request):
    # Logic for generating reports
    return render(request, 'report.html')

