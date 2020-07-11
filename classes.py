
class Person:

    def __init__(self, name='', age=None):
        self.name = name
        self.age = age
    
    def get_age(self):
        your_age = str(self.age)
        return your_age
