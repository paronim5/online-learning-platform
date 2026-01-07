from commands.base.command import Command
from daos.courseDAO import CourseDAO
from utils.logger import log

class ViewTopRatedCoursesCommand(Command):
    def __init__(self, course_dao: CourseDAO):
        self.course_dao = course_dao

    def execute(self) -> bool:
        print("\n--- VIEW: Top Rated Courses ---")
        try:
            data = self.course_dao.get_top_rated_courses_view()
            if not data:
                print("No data found in view.")
                return True

            print(f"{'Course':<30} | {'Instructor':<20} | {'Rating':<6} | {'Level':<12} | {'Price':<8} | {'Students':<8}")
            print("-" * 110)
            for row in data:
                rating = row['instructor_rating'] if row['instructor_rating'] else 0.0
                print(f"{row['course_title']:<30} | {row['instructor_name']:<20} | {rating:<6} | {row['level']:<12} | {row['price']:<8} | {row['total_students']:<8}")
            print("-" * 110)
            return True
        except Exception as e:
            log(f"Error displaying top rated courses: {e}", "ERROR")
            return False

    def undo(self):
        print("Undo not supported for views.")
