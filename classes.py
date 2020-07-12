from datetime import date


class Person:
    def __init__(self, name='', birth=None):
        self.name = name
        self.birth = birth
    
    def get_age(self):
        today = date.today()
        return today.year - self.birth.year - ((today.month, today.day) < (self.birth.month, self.birth.day))
