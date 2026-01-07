# SPSE Jecna Test Case 
 
**Test Case ID:** FUN_02  
**Test Designed by:** Pavlo Kosov 
**Test Name:** Reporting & Data Import  
**Brief description:** Verify the ability to import bulk data from various formats and generate aggregated performance reports.  
**Pre-conditions:** Application is running. Data files (`students.csv`, `instructors.json`, `courses.xml`) exist in `data/` folder.  
**Dependencies and Requirements:** Read permissions for `data/` folder.  
 
| Step | Test Steps | Test Data | Expected Result | Notes |
|------|------------|-----------|-----------------|-------|
| 1 | Navigate to "Import Data" menu. | Select Option `6` | Import options (CSV, JSON, XML) are displayed. | |
| 2 | Import Students from CSV. | File: `data/students.csv` | Message: "Successfully imported X students". | |
| 3 | Import Instructors from JSON. | File: `data/instructors.json` | Message: "Successfully imported X instructors". | |
| 4 | Import Courses from XML. | File: `data/courses.xml` | Message: "Successfully imported X courses". | |
| 5 | Generate "Course Performance Report" via "Advanced Operations". | Select Option `5` | Table displays aggregated data (Avg Score, Min, Max) for courses. | |
| 6 | Verify "Top Rated Courses" view. | Select Option `7` (Advanced) | Table displays courses ordered by Instructor Rating. | |
| 7 | Test Configuration Error Handling (Simulated). | Rename `.env` to `.env.neco` and restart app. | Application shows connection error gracefully, no raw stack trace. | |
