import random
import string
from datetime import date
from models.student import Student
from models.instructor import Instructor
from models.course import Course
from models.enrollment import Enrollment
from models.certificate import Certificate

from daos.studentDAO import StudentDAO
from daos.instructorDAO import InstructorDAO
from daos.courseDAO import CourseDAO
from daos.enrollmentDAO import EnrollmentDAO
from daos.certificateDAO import CertificateDAO

from utils.logger import log

def get_random_email():
    return ''.join(random.choices(string.ascii_lowercase, k=7)) + "@test.com"

def tests():
    # --- 1. TEST INSTRUCTORS ---
    log("--- Testing InstructorDAO ---")
    inst_dao = InstructorDAO()
    email = get_random_email()
    
    # Save
    new_inst = Instructor(name="Dr. Test", email=email, bio="Bio", rating=5.0, is_verified=True)
    inst_dao.save(new_inst)
    
    # Get All & Get By ID
    all_insts = inst_dao.get_all()
    test_inst = all_insts[-1]
    log(f"Created Instructor ID: {test_inst.id}")
    
    # Update
    test_inst.name = "Dr. Updated"
    inst_dao.update(test_inst.id, test_inst)
    log(f"Update successful: {inst_dao.get_by_id(test_inst.id).name}")

    # --- 2. TEST COURSES ---
    log("--- Testing CourseDAO ---")
    course_dao = CourseDAO()
    
    # Save (Assuming your Model handles the Enum 'Intermediate' correctly now)
    new_course = Course(title="Test Course", instructor_id=test_inst.id, price=10.0, duration_hours=5.0, level="Intermediate")
    course_dao.save(new_course)
    
    # Get All & Get By ID
    test_course = course_dao.get_all()[-1]
    log(f"Created Course ID: {test_course.id}")
    
    # Update
    test_course.title = "Updated Course Title"
    course_dao.update(test_course.id, test_course)
    log(f"Update successful: {course_dao.get_by_id(test_course.id).title}")

    # --- 3. TEST STUDENTS ---
    log("--- Testing StudentDAO ---")
    stud_dao = StudentDAO()
    
    # Save
    stud_dao.save(Student(name="Stud Test", email=get_random_email(), registration_date=date.today()))
    test_stud = stud_dao.get_all()[-1]
    log(f"Created Student ID: {test_stud.id}")
    
    # Update
    test_stud.name = "Updated Student"
    stud_dao.update(test_stud.id, test_stud)
    log(f"Update successful: {stud_dao.get_by_id(test_stud.id).name}")

    # --- 4. TEST ENROLLMENTS ---
    log("--- Testing EnrollmentDAO ---")
    enrol_dao = EnrollmentDAO()
    comp_id = (test_stud.id, test_course.id) # Composite Key
    
    # Save
    new_enrol = Enrollment(student_id=test_stud.id, course_id=test_course.id, progress_percentage=10.0, is_completed=False)
    enrol_dao.save(new_enrol)
    
    # Get By ID (using tuple)
    fetched_enrol = enrol_dao.get_by_id(comp_id)
    log(f"Enrollment fetched: Progress is {fetched_enrol.progress_percentage}%")
    
    # Update
    fetched_enrol.progress_percentage = 100.0
    fetched_enrol.is_completed = True
    enrol_dao.update(comp_id, fetched_enrol)
    log(f"Update successful: Completed={enrol_dao.get_by_id(comp_id).is_completed}")

    # --- 5. TEST CERTIFICATES ---
    log("--- Testing CertificateDAO ---")
    cert_dao = CertificateDAO()
    cert_num = "CERT-" + str(random.randint(1000, 9999))
    
    # Save
    new_cert = Certificate(student_id=test_stud.id, course_id=test_course.id, issue_date=date.today(), certificate_number=cert_num, is_verified=True)
    cert_dao.save(new_cert)
    
    # Get All & Get By ID
    test_cert = cert_dao.get_all()[-1]
    log(f"Certificate Number: {cert_dao.get_by_id(test_cert.id).certificate_number}")
    
    # Update
    test_cert.certificate_number += "-REV"
    cert_dao.update(test_cert.id, test_cert)
    log(f"Update successful: {cert_dao.get_by_id(test_cert.id).certificate_number}")

    # --- 6. TEST DELETES (Reverse Order) ---
    log("--- Testing Delete Methods ---")
    
    # Delete Certificate
    log(f"Delete Certificate: {cert_dao.delete(test_cert.id)}")
    
    # Delete Enrollment
    log(f"Delete Enrollment: {enrol_dao.delete(comp_id)}")
    
    # Delete Course
    log(f"Delete Course: {course_dao.delete(test_course.id)}")
    
    # Delete Student
    log(f"Delete Student: {stud_dao.delete(test_stud.id)}")
    
    # Delete Instructor
    log(f"Delete Instructor: {inst_dao.delete(test_inst.id)}")

    log("--- ALL TESTS COMPLETED SUCCESSFULLY ---")

if __name__ == "__main__":
    tests()