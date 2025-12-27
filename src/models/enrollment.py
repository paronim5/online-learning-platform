class Enrollment:
    def __init__(self, student_id, course_id, progress_percentage=0.0, 
                 final_score=None, is_completed=False, enrollment_datetime=None):
        self._student_id = student_id
        self._course_id = course_id
        self.progress_percentage = progress_percentage
        self.final_score = final_score
        self.is_completed = is_completed
        self._enrollment_datetime = enrollment_datetime

    @property
    def progress_percentage(self): return self._progress_percentage

    @progress_percentage.setter
    def progress_percentage(self, value):
        if not (0 <= value <= 100):
            raise ValueError("Progress must be between 0 and 100.")
        self._progress_percentage = float(value)
        # Logic: Auto-complete if progress is 100
        if self._progress_percentage == 100.0:
            self.is_completed = True

    @property
    def final_score(self): return self._final_score

    @final_score.setter
    def final_score(self, value):
        if value is not None and value < 0:
            raise ValueError("Score cannot be negative.")
        self._final_score = value

    def __str__(self):
        return f"Enrollment: Student {self._student_id} in Course {self._course_id} - {self._progress_percentage}%"

    def __eq__(self, other):
        if not isinstance(other, Enrollment): return False
        return (self._student_id == other._student_id and 
                self._course_id == other._course_id)