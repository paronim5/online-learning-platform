import re

class Instructor:
    def __init__(self, name, email, bio=None, rating=0.0, is_verified=False, id=None):
        self._id = id
        self.name = name
        self.email = email
        self.bio = bio
        self.rating = rating
        self.is_verified = is_verified
    @property
    def id(self): return self._id
    @property
    def name(self): return self._name

    @name.setter
    def name(self, value):
        if not value or len(value) > 100:
            raise ValueError("Name must be between 1 and 100 characters.")
        self._name = value

    @property
    def email(self): return self._email

    @email.setter
    def email(self, value):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", value):
            raise ValueError("Invalid email format.")
        self._email = value

    @property
    def rating(self): return self._rating

    @rating.setter
    def rating(self, value):
        if not (0 <= value <= 5):
            raise ValueError("Rating must be between 0 and 5.")
        self._rating = float(value)

    def __str__(self):
        status = "Verified" if self.is_verified else "Unverified"
        return f"Instructor: {self._name} ({status}) - Rating: {self._rating}/5"

    def __eq__(self, other):
        if not isinstance(other, Instructor): return False
        return self.email == other.email