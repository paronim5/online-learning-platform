from datetime import date

class Student:
    def __init__(self, name, email, registration_date=None, id=None):
        self._id = id
        self.name = name
        self.email = email
        self.registration_date = registration_date or date.today()

    @property
    def id(self): return self._id

    @property
    def name(self): return self._name

    @name.setter
    def name(self, value):
        if not value: raise ValueError("Student name cannot be empty.")
        self._name = value

    @property
    def email(self): return self._email

    @email.setter
    def email(self, value):
        if "@" not in value: raise ValueError("Invalid email.")
        self._email = value

    def __str__(self):
        return f"Student: {self._name} (Joined: {self.registration_date})"

    def __eq__(self, other):
        if not isinstance(other, Student): return False
        return self.email == other.email