from enums.courseLevels import CourseLevel

class Course:
    def __init__(self, title, instructor_id, duration_hours, level, price=0.0, id=None):
        self._id = id
        self.title = title             
        self.instructor_id = instructor_id
        self.price = price
        self.duration_hours = duration_hours
        self.level = level

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not value or not isinstance(value, str):
            raise ValueError("Title must be a non-empty string.")
        if len(value) > 200:
            raise ValueError("Title cannot exceed 200 characters.")
        self._title = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("Price must be a positive number.")
        self._price = float(value)

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        if not isinstance(value, CourseLevel):
            raise ValueError(f"Level must be a CourseLevel Enum. Got {type(value)}")
        self._level = value

    @property
    def id(self): 
        return self._id
    
    @property
    def instructor_id(self): 
        return self._instructor_id
    
    @instructor_id.setter
    def instructor_id(self, value):
        if not isinstance(value, int): raise ValueError("Instructor ID must be an integer.")
        self._instructor_id = value

    def __str__(self):
        """Human-readable representation of the object."""
        return f"Course(ID: {self._id}, Title: '{self._title}', Level: {self._level.value}, Price: ${self._price:.2f})"

    def __eq__(self, other):
        """Logic for comparing two course objects (Equality)."""
        if not isinstance(other, Course):
            return False
        return self._id == other._id if self._id else (self._title == other._title and self._instructor_id == other._instructor_id)

