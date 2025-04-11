# Morris Health Services Application

**CS 631 – Morris Health Services Application, Project Deliverable 3**  
*The entire frontend and user guide was generated using ChatGPT.*

---

## Extensions

- **For PDFs:** `vscode-pdf`
- **For Markdown:** *Markdown Preview Enhanced* by Yiyi Wang  
  _Check Details section for shortcuts._
- **For Database Connection:** *MySQL* by Weijan Chen

---

## Key Points

Morris Health Services (MHS) is focused on developing three core applications:

1. **Employee and Facility Management**
2. **Patient Management** (including appointments, procedures, and billing)
3. **Management Reporting**  
   _This is particularly vital for decision-making by management and the Accounting Department._

---

## Features

### 1. Employee and Facility Management

Provides **insert/update/view** utilities for:

- Employees  
- Medical Offices  
- Out-patient Surgery Facilities  
- Employee Assignments  
- Insurance Companies  
- Any additional necessary entities  

---

### 2. Patient Management

Allows for **insert/entry/view** of activities and revenue including:

- Creating new patient records  
- Creating and updating appointments with charges when completed  
- Generating daily insurance company invoices with patient subtotals  

---

### 3. Management and Reporting

Used by management to:

- Review or change operations  
- Manage workforce  
- Measure financial performance  

Provides statistics for analyzing income, facilities, employees, and patients.

#### Specifically, this module performs:

- For a **given day**, generate a report of **revenue (patient charges)** by facility with **subtotals and a total**
- For a **user-selected date and physician**, display a **list of appointments**
- For a **user-selected time period and facility**, generate a **detailed appointment list** including:
  - Date-Time  
  - Physician  
  - Patient  
  - Description  
- For a **user-selected month**, compute the **top 5 best revenue days**
- For a **user-selected time period**, compute the **average daily revenue per insurance company**

---
