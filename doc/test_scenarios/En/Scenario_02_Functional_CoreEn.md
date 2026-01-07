# SPSE Jecna Test Case 
 
**Test Case ID:** FUN_01  
**Test Designed by:** Pavlo Kosov 
**Test Name:** Core Workflow - Register & Enroll  
**Brief description:** Verify the complete flow of registering a new student, creating a course, and enrolling the student using a transaction.  
**Pre-conditions:** Application is running, Database is initialized.  
**Dependencies and Requirements:** None.  
 
| Step | Test Steps | Test Data | Expected Result | Notes |
|------|------------|-----------|-----------------|-------|
| 1 | Create a new Instructor via "Manage Instructors". | Name: `Test Prof`, Email: `prof@test.com`, Rating: `5.0` | Instructor created successfully. ID is displayed. | |
| 2 | Create a new Course via "Manage Courses". | Title: `Test 101`, Price: `100`, Level: `Beginner` | Course created successfully. ID is displayed. | |
| 3 | Navigate to "Advanced Operations" and select "Register New Student & Enroll". | Name: `New Student`, Email: `new@student.com` | Prompts for Course selection. | |
| 4 | Complete the transactional enrollment. | Select Course ID from Step 2. | Success message: "Successfully registered student and enrolled in course." | |
| 5 | Verify Student creation via "Manage Students". | Select "View All Students" | "New Student" appears in the list. | |
| 6 | Verify Enrollment via "Manage Enrollments". | Select "View All Enrollments" | "New Student" is listed for "Test 101" with 0% progress. | |
| 7 | Attempt duplicate registration (Error Handling). | Same data as Step 3. | System displays error (Duplicate Entry/Transaction Failed) but does not crash. | |
