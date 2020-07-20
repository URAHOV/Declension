
class Person:

    def __init__(self, name='', age=None): ## конструктор класса
        self.name = name
        self.age = age
    
    def get_person_data(self):
        your_name = str(self.name)
        your_age = str(self.age)
        return (your_name, your_age) ## получаем кортеж
