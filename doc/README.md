# Online Learning Platform Management System

**Author:** Pavlo Kosov 
**School:** SPSE Ječná  
**Date:** January 9, 2026  
**Project Type:** School Project (RDBMS)

---

## 1. Introduction & Summary

This is a console-based application for managing an **Online Learning Platform**.  
It allows administrators to manage students, instructors, courses, enrollments, and certificate issuance.

The application is built in **Python** and uses **MySQL** database with the **DAO** (Data Access Object) design pattern.

**Main database concept:**  
Management of online courses, students, instructors, enrollments and issued certificates.

## 2. Database & Data Model

**Database technology:** MySQL 8.0+  
**Main design pattern:** DAO + Singleton for database connection

### Main Tables

- `INSTRUCTORS` – instructor details  
- `COURSES` – courses (linked to instructors, 1:N)  
- `STUDENTS` – student/user information  
- `ENROLLMENTS` – many-to-many relationship between students and courses + progress tracking  
- `CERTIFICATES` – certificates issued (1:1 with enrollment, after course completion)

### Entity-Relationship Diagram (ERD)

Database schema created in **Oracle SQL Developer Data Modeler**:

![Database Schema / ER Diagram](img/image.png)

## 3. Functional Requirements / Core Features

The system supports these main operations:

- **Student Management** – register, view, update, delete students  
- **Instructor Management** – manage profiles, ratings, verification status  
- **Course Management** – create courses, assign instructors, set price and difficulty level  
- **Enrollment Management** – enroll students, track progress, record grades  
- **Certificate Issuance** – issue certificates upon course completion  
- **Reporting** – student progress, top-rated courses, performance statistics  
- **Bulk Data Import** – students (CSV), instructors (JSON), courses (XML)

## 4. Project Architecture

- **Language:** Python 3.10+  
- **Database:** MySQL 8.0  
- **Design patterns used:**
  - DAO – separation of business logic from database operations
  - Singleton – single database connection
  - Command Pattern – handling menu actions

### Directory Structure
``` asci
src/
├── models/         # Entity/data classes
├── daos/           # Data Access Objects – SQL operations
├── commands/       # Command pattern implementations for menu
├── utils/          # Helpers (logging, data importers, etc.)
└── main.py         # Application entry point
```


## 5. Installation & Setup

   1. Install **Python 3.10+** and **MySQL Server**  
   2. Install dependencies:
      ```bash
      pip install -r requirements.txt
      ```

   3. Set up database:
   Import database_export.sql
   OR create database online_learning_platform and run schema script manually

   4. Create .env file in project under src/.env:
      ```.env
         DB_HOST=localhost
         DB_USER=root
         DB_PASS=your_password
      ```
   5. Run the application:
      ```bash
      python /src/main.py
      ```
## 6. Data Import Formats

### Students → CSV:
```csv
name,email,registration_date
```
### Instructors → JSON:
```JSON
[
  {"name": "...", "email": "...", "bio": "...", "rating": 4.5, "is_verified": true}
]
```

### Courses → XML:
```XML
<courses>
  <course>
    <title>...</title>
    <instructor_id>1</instructor_id>
    <price>99.99</price>
    <duration>10.5</duration>
    <level>Beginner</level>
  </course>
</courses>
```
## 7. Error Handling & Logging

Database errors are caught in DAO layer
Input validation before database operations
Critical errors are shown to user + detailed logging to log.txt

## 8. Third-Party Libraries & Licenses

mysql-connector-python → Oracle (GPLv2)
python-dotenv → BSD-3-Clause
