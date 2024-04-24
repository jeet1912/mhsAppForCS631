-- facilities 
INSERT INTO FACILITY (Facility_ID, Street, City, State, Zip, MaxSize, Facility_Type) VALUES
('FAC001', '123 Maple St', 'Springfield', 'IL', '62701', 200, 'Hospital'),
('FAC002', '456 Oak St', 'Centerville', 'CA', '90001', 150, 'Clinic'),
('FAC003', '789 Pine St', 'Lakeview', 'TX', '75001', 300, 'Surgical Center'),
('FAC004', '220 Cedar St', 'Riverside', 'FL', '32202', 100, 'Clinic'),
('FAC005', '321 Birch St', 'Greenwood', 'NV', '88901', 250, 'Hospital'),
('FAC006', '432 Spruce St', 'Madison', 'WI', '53703', 150, 'Rehabilitation'),
('FAC007', '533 Willow St', 'Fairview', 'OR', '97024', 200, 'Hospital'),
('FAC008', '634 Elm St', 'Clayton', 'MO', '63105', 170, 'Clinic'),
('FAC009', '735 Ash St', 'Liberty', 'AZ', '85326', 280, 'Surgical Center'),
('FAC010', '836 Hawthorn St', 'Chelsea', 'MA', '02150', 120, 'Clinic');

--office buildings
INSERT INTO OFFICE_BUILDING (Facility_ID, Office_Count) VALUES
('FAC002', 30),
('FAC003', 20),
('FAC008', 25),
('FAC010', 15);

--outpatient surgeries
INSERT INTO OUTPATIENT_SURGERY (Facility_ID, Room_Count, Procedure_Code, Description) VALUES
('FAC003', 5, 'PROC100', 'General Surgery'),
('FAC001', 8, 'PROC200', 'Orthopedic Surgery'),
('FAC009', 7, 'PROC300', 'Plastic Surgery'),
('FAC007', 10, 'PROC400', 'Cardiac Surgery');

--employees
INSERT INTO EMPLOYEE (SSN, FirstName, MiddleName, LastName, Street, City, State, Zip, Salary, Date_Hired, Job_Class, Fac_ID) VALUES
('EMP001', '555-01-2345', 'John', 'A', 'Doe', '101 First St', 'Springfield', 'IL', '62701', 85000.00, '2010-06-15', 'Doctor', 'FAC001'),
('EMP002', '555-02-2346', 'Jane', 'B', 'Smith', '102 Second St', 'Centerville', 'CA', '90001', 65000.00, '2012-07-20', 'Nurse', 'FAC002'),
('EMP003', '555-03-2347', 'Jim', 'C', 'Brown', '103 Third St', 'Lakeview', 'TX', '75001', 75000.00, '2011-08-25', 'Admin', 'FAC003'),
('EMP004', '555-04-2348', 'Elena', 'F', 'Watson', '104 Fourth St', 'Riverside', 'FL', '32202', 95000.00, '2013-09-12', 'Doctor', 'FAC004'),
('EMP005', '555-05-2349', 'Marco', 'G', 'Chen', '105 Fifth St', 'Greenwood', 'NV', '88901', 90000.00, '2014-10-23', 'Doctor', 'FAC005'),
('EMP006', '555-06-2350', 'Lucas', 'H', 'Morris', '106 Sixth St', 'Madison', 'WI', '53703', 70000.00, '2015-11-30', 'Nurse', 'FAC006'),
('EMP007', '555-07-2351', 'Isabella', 'I', 'Garcia', '107 Seventh St', 'Riverside', 'FL', '32202', 68000.00, '2016-12-01', 'Nurse', 'FAC004'),
('EMP008', '555-08-2352', 'Alexander', 'J', 'Kumar', '108 Eighth St', 'Greenwood', 'NV', '88901', 50000.00, '2017-01-15', 'Admin', 'FAC005'),
('EMP009', '555-09-2353', 'Olivia', 'K', 'Williams', '109 Ninth St', 'Fairview', 'OR', '97024', 120000.00, '2018-02-20', 'Doctor', 'FAC007'),
('EMP010', '555-10-2354', 'Ethan', 'L', 'Jones', '110 Tenth St', 'Clayton', 'MO', '63105', 115000.00, '2019-03-18', 'Doctor', 'FAC008'),
('EMP011', '555-11-2355', 'Mia', 'M', 'Brown', '111 Eleventh St', 'Liberty', 'AZ', '85326', 112000.00, '2020-04-22', 'Doctor', 'FAC009'),
('EMP012', '555-12-2356', 'Noah', 'N', 'Davis', '112 Twelfth St', 'Chelsea', 'MA', '02150', 95000.00, '2021-05-25', 'Doctor', 'FAC010'),
('EMP013', '555-13-2357', 'Charlotte', 'O', 'Miller', '113 Thirteenth St', 'Springfield', 'IL', '62701', 70000.00, '2017-06-30', 'Nurse', 'FAC001'),
('EMP014', '555-14-2358', 'Jacob', 'P', 'Wilson', '114 Fourteenth St', 'Centerville', 'CA', '90001', 68000.00, '2018-07-05', 'Nurse', 'FAC002'),
('EMP015', '555-15-2359', 'Amelia', 'Q', 'Martinez', '115 Fifteenth St', 'Lakeview', 'TX', '75001', 50000.00, '2019-08-10', 'Admin', 'FAC003'),
('EMP016', '555-16-2360', 'William', 'R', 'Anderson', '116 Sixteenth St', 'Riverside', 'FL', '32202', 51000.00, '2020-09-15', 'Admin', 'FAC004'),
('EMP017', '555-17-2361', 'Natalie', 'R', 'Black', '117 Seventeenth St', 'Fairview', 'OR', '97024', 60000.00, '2021-02-11', 'HCP', 'FAC007'),
('EMP018', '555-18-2362', 'Carlos', 'S', 'Lopez', '118 Eighteenth St', 'Clayton', 'MO', '63105', 62000.00, '2021-03-15', 'HCP', 'FAC008'),
('EMP019', '555-19-2363', 'Fiona', 'T', 'Chang', '119 Nineteenth St', 'Liberty', 'AZ', '85326', 58000.00, '2021-04-20', 'HCP', 'FAC009'),
('EMP020', '555-20-2364', 'George', 'U', 'Morris', '120 Twentieth St', 'Chelsea', 'MA', '02150', 56000.00, '2021-05-25', 'HCP', 'FAC010'),
('EMP021', '555-21-2365', 'Lily', 'V', 'Evans', '121 Twenty-first St', 'Springfield', 'IL', '62701', 54000.00, '2021-06-30', 'HCP', 'FAC001'),
('EMP022', '555-22-2366', 'Omar', 'W', 'Jenkins', '122 Twenty-second St', 'Centerville', 'CA', '90001', 63000.00, '2021-07-05', 'HCP', 'FAC002');

--doctors
INSERT INTO DOCTOR (EmployeeID, Speciality, Board_Certification_Date) VALUES
('EMP001', 'Cardiology', '2015-05-20'),
('EMP004', 'Dermatology', '2018-08-16'),
('EMP005', 'Pediatrics', '2019-09-17'),
('EMP009', 'Neurology', '2022-02-20'),
('EMP010', 'Orthopedics', '2023-03-18'),
('EMP011', 'Gastroenterology', '2024-04-22'),
('EMP012', 'Endocrinology', '2025-05-25');

--nurses
INSERT INTO NURSE (EmployeeID, Certification) VALUES
('EMP002', 'Registered Nurse'),
('EMP006', 'Certified Clinical Nurse'),
('EMP007', 'Certified Pediatric Nurse'),
('EMP013', 'Certified Geriatric Nurse'),
('EMP014', 'Certified Emergency Nurse');

--admin staff
INSERT INTO ADMIN_STAFF (EmployeeID, Job_Title) VALUES
('EMP003', 'Office Manager'),
('EMP015', 'Billing Specialist'),
('EMP016', 'HR Coordinator');

--other healthcare professionals
INSERT INTO OTHER_HCP (EmployeeID, Practice_Area) VALUES
('EMP017', 'Physical Therapy'),
('EMP018', 'Radiology Technician'),
('EMP019', 'Dietitian'),
('EMP020', 'Respiratory Therapist'),
('EMP021', 'Occupational Therapy'),
('EMP022', 'Phlebotomy Technician');

--insurance companies
INSERT INTO INSURANCE_COMPANY (InsuranceComp_ID, Name, Street, City, State, Zip) VALUES
('INS001', 'HealthCare Plus', '204 Fourth St', 'Springfield', 'IL', '62701'),
('INS002', 'Wellness Insure', '205 Fifth St', 'Centerville', 'CA', '90001'),
('INS003', 'Family Cover', '206 Sixth St', 'Madison', 'WI', '53703'),
('INS004', 'Secure Health', '207 Seventh St', 'Riverside', 'FL', '32202'),
('INS005', 'Lifetime Insurance', '208 Eighth St', 'Greenwood', 'NV', '88901');

--patients
INSERT INTO PATIENT (Patient_ID, FirstName, MiddleName, LastName, Street, City, State, Zip, First_Visit_Date, Doctor_ID, InComp_ID) VALUES
('PAT001', 'Alice', 'D', 'Johnson', '301 Sixth St', 'Lakeview', 'TX', '75001', '2021-03-15', 'EMP001', 'INS001'),
('PAT002', 'Bob', 'E', 'Lee', '302 Seventh St', 'Springfield', 'IL', '62701', '2021-04-16', 'EMP001', 'INS002'),
('PAT003', 'Clara', 'F', 'Thomas', '303 Eighth St', 'Fairview', 'OR', '97024', '2022-05-20', 'EMP009', 'INS003'),
('PAT004', 'Derek', 'G', 'Hill', '304 Ninth St', 'Clayton', 'MO', '63105', '2022-06-22', 'EMP010', 'INS004'),
('PAT005', 'Eva', 'H', 'Scott', '305 Tenth St', 'Liberty', 'AZ', '85326', '2023-07-23', 'EMP011', 'INS005');

--treats
INSERT INTO TREATS (Patient_ID, Doctor_ID) VALUES
('PAT001', 'EMP001'),
('PAT002', 'EMP001'),
('PAT003', 'EMP009'),
('PAT004', 'EMP010'),
('PAT005', 'EMP011');

--invoice
INSERT INTO INVOICE (Inv_ID, InvDate, InComp_ID) VALUES
('INV001', '2022-01-10', 'INS001'),
('INV002', '2022-02-15', 'INS002'),
('INV003', '2022-05-10', 'INS003'),
('INV004', '2022-06-15', 'INS004'),
('INV005', '2023-07-23', 'INS005');

--invoice details
INSERT INTO INVOICE_DETAIL (InvDetailID, Cost, Inv_ID) VALUES
('IVD001', 1200.00, 'INV001'),
('IVD002', 300.00, 'INV002'),
('IVD003', 450.00, 'INV003'),
('IVD004', 600.00, 'INV004'),
('IVD005', 350.00, 'INV005');

--appointments
INSERT INTO MAKES_APPOINTMENT (Pat_ID, Doc_ID, Fac_ID, Date_Time, In_ID) VALUES
('PAT001', 'EMP001', 'FAC001', '2022-03-20 10:00:00', 'INV001'),
('PAT002', 'EMP001', 'FAC001', '2022-04-22 14:00:00', 'INV002'),
('PAT003', 'EMP009', 'FAC007', '2023-05-20 09:30:00', 'INV003'),
('PAT004', 'EMP010', 'FAC008', '2023-06-22 10:00:00', 'INV004'),
('PAT005', 'EMP011', 'FAC009', '2024-07-23 11:45:00', 'INV005');
