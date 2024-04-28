-- Active: 1713861330832@@127.0.0.1@3306@MHS
SELECT d.EmployeeID, e.FirstName, e.LastName 
FROM DOCTOR d
JOIN EMPLOYEE e ON d.EmployeeID = e.EmployeeID;

SELECT * FROM PATIENT;

SELECT * FROM INSURANCE_COMPANY;

SELECT * FROM FACILITY;

SELECT * FROM INSURANCE_COMPANY WHERE Name = 'GoodHealth Ins';

SELECT * FROM INVOICE;
SELECT * FROM INVOICE_DETAIL;
SELECT * FROM MAKES_APPOINTMENT;


-- Debugging Lock Wait Timeout for Update Appointment
SET GLOBAL innodb_lock_wait_timeout = 5000; 
SET innodb_lock_wait_timeout = 5000;
SHOW PROCESSLIST;
KILL 1143;
KILL 1222;
KILL 1238;
KILL 1295;
KILL 1299;
KILL 1299;
-- Temp Solution: killed unncessary threads.

-- killing inacitve threads
SET GLOBAL wait_timeout = 120; 
SET GLOBAL interactive_timeout = 120; 

-- INSIGHTS!
-- NOTE: updated db_utils.py with error handling to close the connection if an error occurs. Too many connections can adversely affect the performance of the database due to unnecessary overhead,
-- and can also lead to the database running out of connections.


SELECT p.`Patient_ID`, p.`FirstName`, i.`InvDate`, ic.`Name`, SUM(id.`Cost`) AS 'TotalCost'
FROM `PATIENT` p
JOIN `MAKES_APPOINTMENT` ma ON p.`Patient_ID` = ma.`Pat_ID`
JOIN `INVOICE_DETAIL` id ON ma.`InD_ID` = id.`InvDetailID`
JOIN `INVOICE` i ON id.`Inv_ID` = i.`Inv_ID`
JOIN `INSURANCE_COMPANY` ic ON p.`InComp_ID` = ic.`InsuranceComp_ID`
GROUP BY i.`InvDate`, ic.`Name`, p.`Patient_ID`
ORDER BY i.`InvDate` DESC;
