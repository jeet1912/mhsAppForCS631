INSERT INTO FACILITY (Street, City, State, Zip, MaxSize, Facility_Type) VALUES
('123 Main St', 'Springfield', 'IL', '62701', 150, 'Office'),
('124 Main St', 'Springfield', 'IL', '62702', 100, 'Office'),
('125 Main St', 'Springfield', 'IL', '62703', 200, 'Office'),
('126 Main St', 'Springfield', 'IL', '62704', 120, 'Office'),
('127 Main St', 'Springfield', 'IL', '62705', 130, 'Office'),
('128 Main St', 'Springfield', 'IL', '62706', 140, 'Office'),
('129 Main St', 'Springfield', 'IL', '62707', 110, 'Office'),
('130 Main St', 'Springfield', 'IL', '62708', 160, 'Office'),
('131 Main St', 'Springfield', 'IL', '62709', 170, 'Office'),
('132 Main St', 'Springfield', 'IL', '62710', 180, 'Office'),
('133 Main St', 'Springfield', 'IL', '62711', 190, 'Office'),
('134 Pine St', 'Lakeview', 'TX', '75001', 80, 'OP Surgery'),
('135 Pine St', 'Lakeview', 'TX', '75002', 90, 'OP Surgery'),
('136 Pine St', 'Lakeview', 'TX', '75003', 75, 'OP Surgery'),
('137 Pine St', 'Lakeview', 'TX', '75004', 65, 'OP Surgery'),
('138 Pine St', 'Lakeview', 'TX', '75005', 85, 'OP Surgery'),
('139 Pine St', 'Lakeview', 'TX', '75006', 95, 'OP Surgery'),
('140 Pine St', 'Lakeview', 'TX', '75007', 70, 'OP Surgery'),
('141 Pine St', 'Lakeview', 'TX', '75008', 60, 'OP Surgery');

INSERT INTO OFFICE_BUILDING (Facility_ID, Office_Count) VALUES
(1, 10),
(2, 9),
(3, 8),
(4, 7),
(5, 6),
(6, 5),
(7, 4),
(8, 3),
(9, 2),
(10, 1),
(11, 3);

INSERT INTO OUTPATIENT_SURGERY (Facility_ID, Room_Count, Procedure_Code) VALUES
(12, 10, '12345'),
(13, 9, '23456'),
(14, 8, '34567'),
(15, 7, '45678'),
(16, 6, '56789'),
(17, 5, '67890'),
(18, 4, '78901'),
(19, 3, '89012'); 

INSERT INTO INSURANCE_COMPANY (Name, Street, City, State, Zip) VALUES
('GoodHealth Ins', '100 Health Blvd', 'Capital City', 'DC', '20001'),
('SecureLife', '200 Wellness Dr', 'Oldtown', 'OK', '73034'),
('FamilyCare', '300 Safe St', 'Trustville', 'CA', '94016'),
('BudgetShield', '400 Cover Rd', 'Savecity', 'NY', '10001');

INSERT INTO EMPLOYEE (SSN, FirstName, MiddleName, LastName, Street, City, State, Zip, Salary, Date_Hired, Job_Class, Fac_ID) VALUES
('123456789', 'John', 'D', 'Doe', '123 Work St', 'Worktown', 'CA', '94016', 120000.00, '2020-01-10', 'Doctor', 1),
('987654321', 'Jane', 'E', 'Smith', '456 Job Ave', 'Jobville', 'NY', '10001', 95000.00, '2021-02-15', 'Nurse', 2),
('234567890', 'Emily', 'F', 'Jones', '789 Career Blvd', 'Workcity', 'TX', '75001', 50000.00, '2022-03-10', 'Admin', 3),
('345678901', 'Michael', 'G', 'Brown', '101 Admin Rd', 'Adminville', 'FL', '32250', 60000.00, '2020-04-20', 'HCP', 1),
('456789012', 'Chloe', 'H', 'Davis', '202 Staff St', 'Stafftown', 'CA', '94016', 120000.00, '2020-05-15', 'Doctor', 4),
('567890123', 'Luke', 'I', 'Wilson', '303 Job Way', 'Jobburgh', 'NY', '10001', 95000.00, '2021-06-18', 'Nurse', 5),
('678901234', 'Olivia', 'J', 'Martinez', '404 Career Ct', 'Workshire', 'TX', '75001', 50000.00, '2022-07-22', 'Admin', 2),
('789012345', 'James', 'K', 'Taylor', '505 Admin Ave', 'Adminburg', 'FL', '32250', 60000.00, '2020-08-25', 'HCP', 3),
('890123456', 'Isabella', 'L', 'Thomas', '606 Staff Rd', 'Staffville', 'CA', '94016', 120000.00, '2020-09-28', 'Doctor', 6),
('901234567', 'Ethan', 'M', 'Harris', '707 Job Ln', 'Jobland', 'NY', '10001', 95000.00, '2021-10-30', 'Nurse', 7),
('012345678', 'Sophia', 'N', 'Moore', '808 Career Way', 'Worktown', 'TX', '75001', 50000.00, '2022-11-01', 'Admin', 4),
('123456780', 'Jacob', 'O', 'Jackson', '909 Admin St', 'Admincity', 'FL', '32250', 60000.00, '2020-12-03', 'HCP', 5),
('234567891', 'Mia', 'P', 'Lee', '121 Staff Ave', 'Staffshire', 'CA', '94016', 120000.00, '2021-01-04', 'Doctor', 8),
('345678902', 'William', 'Q', 'Anderson', '232 Job Rd', 'Jobville', 'NY', '10001', 95000.00, '2022-02-05', 'Nurse', 9),
('456789013', 'Ava', 'R', 'Thomas', '343 Career Blvd', 'Workcity', 'TX', '75001', 50000.00, '2023-03-07', 'Admin', 6),
('567890124', 'Noah', 'S', 'Miller', '454 Admin Way', 'Adminburgh', 'FL', '32250', 60000.00, '2024-04-08', 'HCP', 7),
('678901235', 'Lily', 'T', 'Davis', '565 Staff Ct', 'Stafftown', 'CA', '94016', 120000.00, '2025-05-10', 'Doctor', 10),
('789012346', 'Benjamin', 'U', 'Wilson', '676 Job Ave', 'Jobshire', 'NY', '10001', 95000.00, '2026-06-11', 'Nurse', 11),
('890123457', 'Emma', 'V', 'Martinez', '787 Career Rd', 'Workville', 'TX', '75001', 50000.00, '2027-07-13', 'Admin', 8),
('901234568', 'Jack', 'W', 'Taylor', '898 Admin Ln', 'Adminland', 'FL', '32250', 60000.00, '2028-08-14', 'HCP', 9);

INSERT INTO DOCTOR (EmployeeID, Speciality, Board_Certification_Date) VALUES
(1, 'Cardiology', '2020-01-10'),
(5, 'Dermatology', '2020-05-15'),
(9, 'Endocrinology', '2020-09-28'),
(13, 'Gastroenterology', '2021-01-04'),
(17, 'Hematology', '2021-05-10');

INSERT INTO NURSE (EmployeeID, Certification) VALUES
(2, 'RN'),
(6, 'LPN'),
(10, 'CNA'),
(14, 'RN'),
(18, 'LPN');

INSERT INTO ADMIN_STAFF (EmployeeID, Job_Title) VALUES
(3, 'Receptionist'),
(7, 'Secretary'),
(11, 'Clerk'),
(15, 'Receptionist'),
(19, 'Secretary');

INSERT INTO OTHER_HCP (EmployeeID, Practice_Area) VALUES
(4, 'Physical Therapy'),
(8, 'Occupational Therapy'),
(12, 'Speech Therapy'),
(16, 'Physical Therapy'),
(20, 'Occupational Therapy');

INSERT INTO PATIENT (FirstName, MiddleName, LastName, Street, City, State, Zip, First_Visit_Date, Doctor_ID, InComp_ID) VALUES
('Alice', 'F', 'Johnson', '789 Patient Rd', 'Healtown', 'FL', '32250', '2023-01-10', 1, 1),
('Bob', 'G', 'Lee', '101 Recovery Ln', 'Medcity', 'TX', '75070', '2023-02-20', 5, 1),
('Charlie', 'H', 'Clark', '234 Health St', 'Wellville', 'CA', '94016', '2023-03-15', 9, 2),
('Diana', 'I', 'Wright', '345 Care Ave', 'Curetown', 'NY', '10001', '2023-04-10', 13, 2),
('Evan', 'J', 'Morris', '456 Wellness Blvd', 'Aidcity', 'VA', '24502', '2023-05-05', 17, 3),
('Fiona', 'K', 'Smith', '567 Help Rd', 'Nursetown', 'NC', '27514', '2023-06-21', 1, 3),
('George', 'L', 'Baker', '678 Assist St', 'Recoveryville', 'GA', '30301', '2023-07-15', 5, 4),
('Hannah', 'M', 'Gonzalez', '789 Heal Ln', 'Therapytown', 'MA', '02101', '2023-08-10', 9, 4),
('Ian', 'N', 'Davis', '890 Save Ave', 'Doccity', 'AZ', '85001', '2023-09-20', 13, 1),
('Julia', 'O', 'Martinez', '901 Medicine Rd', 'Clinictown', 'IL', '60007', '2023-10-15', 17, 2);

INSERT INTO INVOICE (InvDate, InComp_ID) VALUES
('2023-01-15', 1),
('2023-02-20', 1),
('2023-03-18', 2),
('2023-04-22', 2),
('2023-05-10', 3),
('2023-06-15', 3),
('2023-07-20', 4),
('2023-08-25', 4),
('2023-09-30', 1),
('2023-10-05', 2);

INSERT INTO INVOICE_DETAIL (Cost, Inv_ID) VALUES
(150.00, 1),
(200.00, 2),
(175.00, 3),
(180.00, 4),
(190.00, 5),
(160.00, 6),
(210.00, 7),
(200.00, 8),
(195.00, 9),
(205.00, 10);

INSERT INTO MAKES_APPOINTMENT (Pat_ID, Doc_ID, Fac_ID, Date_Time, InD_ID) VALUES
(1, 1, 1, '2023-01-14 09:00:00', 1),
(2, 5, 2, '2023-02-19 10:00:00', 2),
(3, 9, 3, '2023-03-17 11:00:00', 3),
(4, 13, 4, '2023-04-21 12:00:00', 4),
(5, 17, 5, '2023-05-09 13:00:00', 5),
(6, 1, 6, '2023-06-14 14:00:00', 6),
(7, 5, 7, '2023-07-19 15:00:00', 7),
(8, 9, 8, '2023-08-24 16:00:00', 8),
(9, 13, 9, '2023-09-29 17:00:00', 9),
(10, 17, 10, '2023-10-04 18:00:00', 10);

INSERT INTO TREATS (Patient_ID, Doctor_ID) VALUES
(1, 1),
(2, 5),
(3, 9),
(4, 13),
(5, 17),
(6, 1),
(7, 5),
(8, 9),
(9, 13),
(10, 17);


INSERT INTO INVOICE VALUES 
(1,'2024-04-28',1, 0),(2,'2024-04-29',1, 0),(3,'2024-04-30',1, 0),(4,'2024-05-01',1, 0),(5,'2024-05-02',2, 0),(6,'2024-04-29',2, 0),(7,'2024-05-01',3, 0),(8,'2024-04-29',3, 0),(9,'2024-04-30',2, 0);

INSERT INTO INVOICE_DETAIL
VALUES (1,432.00,1),(2,421.00,1),(3,543.00,2),(4,521.00,3),(5,345.00,4),(6,234.00,1),(7,531.00,4),(8,453.00,5),(9,432.00,6),(10,42.00,7),(11,342.00,8),(12,789.00,2),(13,468.00,9),(14,759.00,9),(15,1000.00,5),(16,1000.00,3),(17,1000.00,5);

INSERT INTO MAKES_APPOINTMENT
VALUES (2,5,2,'2024-04-28 04:00:00',1),(1,1,1,'2024-04-29 03:33:00',2),(1,9,3,'2024-04-29 04:00:00',3),(1,1,1,'2024-04-30 07:45:00',4),(1,1,1,'2024-05-01 09:55:00',5),(1,9,1,'2024-04-28 09:55:00',6),(1,17,11,'2024-05-01 04:00:00',7),(3,9,15,'2024-05-03 03:33:00',8),(4,5,7,'2024-04-29 15:11:00',9),(5,5,5,'2024-05-01 08:00:00',10),(6,13,17,'2024-04-29 10:44:00',11),(9,9,8,'2024-04-29 07:44:00',12),(10,5,19,'2024-04-30 12:40:00',13),(10,9,8,'2024-05-01 03:00:00',14),(10,13,4,'2024-05-02 04:00:00',15),(1,13,5,'2024-04-30 04:55:00',16),(3,9,9,'2024-05-03 03:00:00',17);