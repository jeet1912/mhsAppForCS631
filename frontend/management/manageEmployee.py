from .db_utils import execute_query


def get_current_job_class(employee_id):
    # Query the database to retrieve the current job class of the employee
    sql = "SELECT Job_Class FROM EMPLOYEE WHERE EmployeeID = %s"
    result = execute_query(sql, params=(employee_id,), fetchone=True)
    if result:
        return result['Job_Class']
    return None

def delete_old_entry(employee_id, current_job_class):
    # Delete the old entry from the respective table based on the current job class
    if current_job_class == 'Doctor':
        sql = "DELETE FROM DOCTOR WHERE EmployeeID = %s"
    elif current_job_class == 'Nurse':
        sql = "DELETE FROM NURSE WHERE EmployeeID = %s"
    elif current_job_class == 'HCP':
        sql = "DELETE FROM OTHER_HCP WHERE EmployeeID = %s"
    elif current_job_class == 'Admin':
        sql = "DELETE FROM ADMIN_STAFF WHERE EmployeeID = %s"
    execute_query(sql, params=(employee_id,))

def insert_doctor_details(employee_id, speciality, board_certification_date):
    # Insert new entry into the Doctor table
    sql = """
    INSERT INTO DOCTOR (EmployeeID, Speciality, Board_Certification_Date)
    VALUES (%s, %s, %s)
    """
    params = (employee_id, speciality, board_certification_date)
    return execute_query(sql, params=params)

def update_doctor_details(employee_id, speciality, board_certification_date):
    # Update existing entry in the Doctor table
    sql = """
    UPDATE DOCTOR
    SET Speciality = %s, Board_Certification_Date = %s
    WHERE EmployeeID = %s
    """
    params = (speciality, board_certification_date, employee_id)
    return execute_query(sql, params=params)

def insert_nurse_details(employee_id, certification):
    # Insert new entry into the Nurse table
    sql = """
    INSERT INTO NURSE (EmployeeID, Certification)
    VALUES (%s, %s)
    """
    params = (employee_id, certification)
    return execute_query(sql, params=params)

def update_nurse_details(employee_id, certification):
    # Update existing entry in the Nurse table
    sql = """
    UPDATE NURSE
    SET Certification = %s
    WHERE EmployeeID = %s
    """
    params = (certification, employee_id)
    return execute_query(sql, params=params)

def insert_other_hcp_details(employee_id, practice_area):
    # Insert new entry into the Other HCP table
    sql = """
    INSERT INTO OTHER_HCP (EmployeeID, Practice_Area)
    VALUES (%s, %s)
    """
    params = (employee_id, practice_area)
    return execute_query(sql, params=params)

def update_other_hcp_details(employee_id, practice_area):
    # Update existing entry in the Other HCP table
    sql = """
    UPDATE OTHER_HCP
    SET Practice_Area = %s
    WHERE EmployeeID = %s
    """
    params = (practice_area, employee_id)
    return execute_query(sql, params=params)

def insert_admin_staff_details(employee_id, job_title):
    # Insert new entry into the Admin Staff table
    sql = """
    INSERT INTO ADMIN_STAFF (EmployeeID, Job_Title)
    VALUES (%s, %s)
    """
    params = (employee_id, job_title)
    return execute_query(sql, params=params)

def update_admin_staff_details(employee_id, job_title):
    # Update existing entry in the Admin Staff table
    sql = """
    UPDATE ADMIN_STAFF
    SET Job_Title = %s
    WHERE EmployeeID = %s
    """
    params = (job_title, employee_id)
    return execute_query(sql, params=params)


def update_employee_details(employee_id, job_class, **kwargs):
    result = None
    
    current_job_class = get_current_job_class(employee_id)
    if current_job_class != job_class:
        print(current_job_class, job_class)
        delete_old_entry(employee_id, current_job_class)
        
        # Insert new entry into the updated class table
        if job_class == 'Doctor':
            result = insert_doctor_details(employee_id, **kwargs)
        elif job_class == 'Nurse':
            result = insert_nurse_details(employee_id, **kwargs)
        elif job_class == 'HCP':
            result = insert_other_hcp_details(employee_id, **kwargs)
        elif job_class == 'Admin':
            result = insert_admin_staff_details(employee_id, **kwargs)
    else:
        # Update existing entry in the same class table
        if job_class == 'Doctor':
            result = update_doctor_details(employee_id, **kwargs)
        elif job_class == 'Nurse':
            result = update_nurse_details(employee_id, **kwargs)
        elif job_class == 'HCP':
            result = update_other_hcp_details(employee_id, **kwargs)
        elif job_class == 'Admin':
            result = update_admin_staff_details(employee_id, **kwargs)
    
    return result
