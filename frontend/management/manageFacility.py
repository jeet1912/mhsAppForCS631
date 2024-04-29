from .db_utils import execute_query


def get_current_facility_type(facility_id):
    # Query the database to retrieve the current facility type of the facility
    sql = "SELECT Facility_Type FROM FACILITY WHERE Facility_ID = %s"
    result = execute_query(sql, params=(facility_id,), fetchone=True)
    if result:
        return result['Facility_Type']
    return None

def delete_old_facility_details(facility_id, current_facility_type):
    # Delete the old entry from the specific table based on the current facility type
    if current_facility_type == 'Office':
        sql = "DELETE FROM OFFICE_BUILDING WHERE Facility_ID = %s"
    elif current_facility_type == 'OP Surgery':
        sql = "DELETE FROM OUTPATIENT_SURGERY WHERE Facility_ID = %s"
    execute_query(sql, params=(facility_id,))

def insert_office_details(facility_id, office_count):
    # Insert new entry into the Office Building table
    sql = """
    INSERT INTO OFFICE_BUILDING (Facility_ID, Office_Count)
    VALUES (%s, %s)
    """
    params = (facility_id, office_count)
    return execute_query(sql, params=params)

def insert_ops_details(facility_id, room_count, procedure_code, description):
    # Insert new entry into the Outpatient Surgery table
    sql = """
    INSERT INTO OUTPATIENT_SURGERY (Facility_ID, Room_Count, Procedure_Code, Description)
    VALUES (%s, %s, %s, %s)
    """
    params = (facility_id, room_count, procedure_code, description)
    return execute_query(sql, params=params)

def update_office_details(facility_id, office_count):
    # Update existing entry in the Office Building table
    sql = """
    UPDATE OFFICE_BUILDING
    SET Office_Count = %s
    WHERE Facility_ID = %s
    """
    params = (office_count, facility_id)
    return execute_query(sql, params=params)

def update_ops_details(facility_id, room_count, procedure_code, description):
    # Update existing entry in the Outpatient Surgery table
    sql = """
    UPDATE OUTPATIENT_SURGERY
    SET Room_Count = %s, Procedure_Code = %s, Description = %s
    WHERE Facility_ID = %s
    """
    params = (room_count, procedure_code, description, facility_id)
    return execute_query(sql, params=params)