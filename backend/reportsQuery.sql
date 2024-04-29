SELECT ic.Name as Name, SUM(inv.Total_Cost) / 3   as Average_Cost 
FROM INVOICE inv
JOIN INSURANCE_COMPANY ic ON inv.InComp_ID = ic.InsuranceComp_ID
WHERE inv.InvDate BETWEEN '2024-05-01' AND '2024-05-03' 
GROUP BY inv.InComp_ID;


SELECT SUM(inv.Total_Cost) as Total_Revenue, inv.InvDate as InvDate
FROM INVOICE inv
WHERE YEAR(inv.InvDate) = 2024 and MONTH(inv.InvDate) = 04
GROUP BY inv.InvDate
ORDER BY Total_Revenue DESC
LIMIT 5;


SELECT DATE(ma.Date_Time) as Date, TIME(ma.Date_Time) as Time,  d.EmployeeID as Doctor_ID, e.FirstName as Doctor, p.Patient_ID as Patient_ID, p.FirstName as Patient, ma.Reason as Description
FROM MAKES_APPOINTMENT ma 
JOIN DOCTOR d ON ma.Doc_ID = d.EmployeeID
JOIN EMPLOYEE e ON d.EmployeeID = e.EmployeeID
JOIN PATIENT p ON ma.Pat_ID = p.Patient_ID
JOIN FACILITY f ON ma.Fac_ID = f.Facility_ID
WHERE (ma.Date_Time BETWEEN '2024-04-28' AND '2024-05-03') AND f.Facility_ID = 1;