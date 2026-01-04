import sys
import os

# Add the current directory to sys.path to ensure imports work when running directly
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.append(current_dir)

from daos.studentDAO import StudentDAO
from daos.courseDAO import CourseDAO
from daos.instructorDAO import InstructorDAO
from daos.enrollmentDAO import EnrollmentDAO
from daos.certificateDAO import CertificateDAO

from services.advanced_service import AdvancedService

from commands.base.invoker import CommandInvoker

# Import all concrete commands
from commands.students.create_student import CreateStudentCommand
from commands.students.view_students import ViewStudentsCommand
from commands.students.update_student import UpdateStudentCommand
from commands.students.delete_student import DeleteStudentCommand

from commands.instructors.create_instructor import CreateInstructorCommand
from commands.instructors.view_instructors import ViewInstructorsCommand
from commands.instructors.update_instructor import UpdateInstructorCommand
from commands.instructors.delete_instructor import DeleteInstructorCommand

from commands.courses.create_course import CreateCourseCommand
from commands.courses.view_courses import ViewCoursesCommand
from commands.courses.update_course import UpdateCourseCommand
from commands.courses.delete_course import DeleteCourseCommand

from commands.enrollments.create_enrollment import CreateEnrollmentCommand
from commands.enrollments.view_enrollments import ViewEnrollmentsCommand
from commands.enrollments.update_enrollment import UpdateEnrollmentCommand
from commands.enrollments.delete_enrollment import DeleteEnrollmentCommand

from commands.certificates.create_certificate import CreateCertificateCommand
from commands.certificates.view_certificates import ViewCertificatesCommand
from commands.certificates.update_certificate import UpdateCertificateCommand
from commands.certificates.delete_certificate import DeleteCertificateCommand

from commands.multiTable.register_student_enrollment import RegisterStudentToCourseCommand
from commands.multiTable.view_detailed_enrollments import ViewDetailedEnrollmentsCommand
from commands.multiTable.update_student_enrollment import UpdateStudentEnrollmentCommand
from commands.multiTable.delete_student_cascade import DeleteStudentCascadeCommand

from utils.logger import logger
from utils.importer import DataImporter

def main():
    try:
        student_dao = StudentDAO()
        course_dao = CourseDAO()
        instructor_dao = InstructorDAO()
        enrollment_dao = EnrollmentDAO()
        certificate_dao = CertificateDAO()
        
        advanced_service = AdvancedService()
        
        importer = DataImporter()
    except Exception as e:
        logger.error(f"Failed to initialize DAOs or Importer: {e}")
        return

    invoker = CommandInvoker()

    while True:
        print("\n=== Learning Platform Management System ===")
        print("1. Manage Students")
        print("2. Manage Instructors")
        print("3. Manage Courses")
        print("4. Manage Enrollments")
        print("5. Manage Certificates")
        print("6. Import Data")
        print("7. Advanced Operations (Multi-table)")
        print("8. Undo Last Action (Global)")
        print("9. Exit")
        
        choice = input("Select Table/Option: ")

        if choice == '9':
            logger.info("Goodbye!")
            break
        elif choice == '8':
            invoker.undo_last_command()
            continue
        elif choice == '6':
            print("\n--- IMPORT DATA ---")
            print("1. Import Students (CSV)")
            print("2. Import Instructors (JSON)")
            print("3. Import Courses (XML)")
            print("B. Back to Main Menu")
            
            imp_choice = input("Select Import Option: ").strip().upper()
            if imp_choice == 'B':
                continue
            
            file_path = input("Enter full file path: ").strip('"')
            
            if imp_choice == '1':
                importer.import_students_from_csv(file_path)
            elif imp_choice == '2':
                importer.import_instructors_from_json(file_path)
            elif imp_choice == '3':
                importer.import_courses_from_xml(file_path)
            else:
                logger.warning("Invalid import option.")
            continue
        elif choice == '7':
            print("\n--- ADVANCED OPERATIONS (Multi-table) ---")
            print("1. Register New Student & Enroll (Transaction)")
            print("2. View Detailed Enrollments (Join)")
            print("3. Update Student & Enrollment (Transaction)")
            print("4. Delete Student & Enrollments (Cascade Transaction)")
            print("B. Back to Main Menu")

            adv_choice = input("Select Operation: ").strip().upper()
            if adv_choice == 'B':
                continue
            
            cmd = None
            if adv_choice == '1':
                cmd = RegisterStudentToCourseCommand(student_dao)
            elif adv_choice == '2':
                cmd = ViewDetailedEnrollmentsCommand(enrollment_dao)
            elif adv_choice == '3':
                cmd = UpdateStudentEnrollmentCommand(enrollment_dao)
            elif adv_choice == '4':
                cmd = DeleteStudentCascadeCommand(student_dao)
            
            if cmd:
                invoker.execute_command(cmd)
            else:
                logger.warning("Invalid option.")
            continue

        # Sub-menus
        context_name = ""
        commands = {} # map '1', '2', etc. to Command Instances

        if choice == '1':
            context_name = "STUDENTS"
            commands = {
                '1': CreateStudentCommand(student_dao),
                '2': ViewStudentsCommand(student_dao),
                '3': UpdateStudentCommand(student_dao),
                '4': DeleteStudentCommand(student_dao)
            }
        elif choice == '2':
            context_name = "INSTRUCTORS"
            commands = {
                '1': CreateInstructorCommand(instructor_dao),
                '2': ViewInstructorsCommand(instructor_dao),
                '3': UpdateInstructorCommand(instructor_dao),
                '4': DeleteInstructorCommand(instructor_dao)
            }
        elif choice == '3':
            context_name = "COURSES"
            commands = {
                '1': CreateCourseCommand(course_dao),
                '2': ViewCoursesCommand(course_dao),
                '3': UpdateCourseCommand(course_dao),
                '4': DeleteCourseCommand(course_dao)
            }
        elif choice == '4':
            context_name = "ENROLLMENTS"
            commands = {
                '1': CreateEnrollmentCommand(enrollment_dao),
                '2': ViewEnrollmentsCommand(enrollment_dao),
                '3': UpdateEnrollmentCommand(enrollment_dao),
                '4': DeleteEnrollmentCommand(enrollment_dao)
            }
        elif choice == '5':
            context_name = "CERTIFICATES"
            commands = {
                '1': CreateCertificateCommand(certificate_dao),
                '2': ViewCertificatesCommand(certificate_dao),
                '3': UpdateCertificateCommand(certificate_dao),
                '4': DeleteCertificateCommand(certificate_dao)
            }
        else:
            logger.warning("[!] Invalid option.")
            continue

        print(f"\n--- {context_name} OPERATIONS ---")
        print("1. Create")
        print("2. View List")
        print("3. Update")
        print("4. Delete")
        print("B. Back to Main Menu")
        
        op_choice = input("Select Operation: ").strip().upper()
        if op_choice == 'B':
            continue
            
        cmd = commands.get(op_choice)
        if cmd:
            invoker.execute_command(cmd)
        else:
            logger.warning("Invalid operation.")

if __name__ == "__main__":
    main()
