# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """
    def __init__(self, name, birth):
        """ make a person checking their name and date of birth"""
        if not isinstance(name, str):
             raise TypeError("name should be a string")
        if name == (""):
             raise ValueError("name cant be empty")
        if not isinstance(birth, date):
            raise TypeError("must be a date")
        self.name = name
        self.birth = birth
            

    def initials(self):
        """ show uppercase initials of persons name """
        return "".join(word[0].upper() for word in self.name.split())
          
    def is_birthday(self):
        """check if today is persons birthdate"""
        today = date.today()
        return self.birth.month == today.month and self.birth.day == today.day

    # (see README.md for further details)