from commands.base.command import Command
from daos.enrollmentDAO import EnrollmentDAO
from utils.logger import log

class GeneratePerformanceReportCommand(Command):
    def __init__(self, enrollment_dao: EnrollmentDAO):
        self.enrollment_dao = enrollment_dao

    def execute(self) -> bool:
        print("\n--- Course Performance Report ---")
        try:
            report_data = self.enrollment_dao.get_course_performance_report()
            
            if not report_data:
                print("No data available for report.")
                return True

            print(f"{'Course':<30} | {'Instructor':<20} | {'Students':<10} | {'Avg Score':<10} | {'Min':<5} | {'Max':<5}")
            print("-" * 95)
            
            for row in report_data:
                avg = row['average_score'] if row['average_score'] is not None else 0.0
                min_s = row['min_score'] if row['min_score'] is not None else 0.0
                max_s = row['max_score'] if row['max_score'] is not None else 0.0
                
                print(f"{row['course_title']:<30} | {row['instructor_name']:<20} | {row['total_students']:<10} | {avg:<10.2f} | {min_s:<5} | {max_s:<5}")
            
            print("-" * 95)
            log("Course performance report displayed successfully.")
            return True
        except Exception as e:
            log(f"Failed to generate report: {e}", "ERROR")
            return False

    def undo(self):
        print("Undo not supported for view operations.")
