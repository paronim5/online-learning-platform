import csv
import json
import xml.etree.ElementTree as ET
from typing import List, Dict, Any
import os

from models.student import Student
from models.instructor import Instructor
from models.course import Course
from daos.studentDAO import StudentDAO
from daos.instructorDAO import InstructorDAO
from daos.courseDAO import CourseDAO
from utils.logger import log

class DataImporter:
    def __init__(self):
        self.student_dao = StudentDAO()
        self.instructor_dao = InstructorDAO()
        self.course_dao = CourseDAO()

    def import_students_from_csv(self, file_path: str) -> int:
        """
        Imports students from a CSV file.
        Expected CSV format: name,email,registration_date
        Returns the number of students successfully imported.
        """
        if not os.path.exists(file_path):
            log(f"File not found: {file_path}", "ERROR")
            return 0

        count = 0
        try:
            with open(file_path, mode='r', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    try:
                        student = Student(
                            name=row['name'],
                            email=row['email'],
                            registration_date=row.get('registration_date')
                        )
                        self.student_dao.save(student)
                        count += 1
                    except Exception as e:
                        log(f"Failed to import student row {row}: {e}", "ERROR")
            log(f"Successfully imported {count} students from {file_path}")
        except Exception as e:
            log(f"Error reading CSV file {file_path}: {e}", "ERROR")
        
        return count

    def import_instructors_from_json(self, file_path: str) -> int:
        """
        Imports instructors from a JSON file.
        Expected JSON format: List of objects with name, email, bio, rating, is_verified
        Returns the number of instructors successfully imported.
        """
        if not os.path.exists(file_path):
            log(f"File not found: {file_path}", "ERROR")
            return 0

        count = 0
        try:
            with open(file_path, mode='r', encoding='utf-8') as jsonfile:
                data = json.load(jsonfile)
                if not isinstance(data, list):
                    log(f"JSON data must be a list of objects.", "ERROR")
                    return 0

                for item in data:
                    try:
                        instructor = Instructor(
                            name=item['name'],
                            email=item['email'],
                            bio=item.get('bio'),
                            rating=item.get('rating', 0.0),
                            is_verified=item.get('is_verified', False)
                        )
                        self.instructor_dao.save(instructor)
                        count += 1
                    except Exception as e:
                        log(f"Failed to import instructor item {item}: {e}", "ERROR")
            log(f"Successfully imported {count} instructors from {file_path}")
        except Exception as e:
            log(f"Error reading JSON file {file_path}: {e}", "ERROR")

        return count

    def import_courses_from_xml(self, file_path: str) -> int:
        """
        Imports courses from an XML file.
        Expected XML format:
        <courses>
            <course>
                <title>...</title>
                <instructor_id>...</instructor_id>
                <price>...</price>
                <duration_hours>...</duration_hours>
                <level>...</level>
            </course>
        </courses>
        Returns the number of courses successfully imported.
        """
        if not os.path.exists(file_path):
            log(f"File not found: {file_path}", "ERROR")
            return 0

        count = 0
        try:
            tree = ET.parse(file_path)
            root = tree.getroot()
            
            if root.tag != 'courses':
                log(f"Root element must be 'courses', found '{root.tag}'", "ERROR")
                return 0

            for course_elem in root.findall('course'):
                try:
                    title = course_elem.find('title').text
                    instructor_id = int(course_elem.find('instructor_id').text)
                    price = float(course_elem.find('price').text)
                    duration_hours = float(course_elem.find('duration_hours').text)
                    level = course_elem.find('level').text

                    course = Course(
                        title=title,
                        instructor_id=instructor_id,
                        price=price,
                        duration_hours=duration_hours,
                        level=level
                    )
                    self.course_dao.save(course)
                    count += 1
                except Exception as e:
                    log(f"Failed to import course element: {e}", "ERROR")
            log(f"Successfully imported {count} courses from {file_path}")
        except Exception as e:
            log(f"Error reading XML file {file_path}: {e}", "ERROR")

        return count
