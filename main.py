## В.13 з.1. Написать программу, которая после введенного с клавиатуры возраста человека,
## дописывала бы слово «год» в правильной форме. Напр: 3 года, 21 год, 45 лет.
## Если число оканчивается на 1, то "год".
## Если на 2,3,4, то "года". Если на 0,5,6,7,8,9, то "лет".

from classes import *

person = Person()

while person.name == '':
    try:
        person.name = str(input("ВВЕДИТЕ СВОЁ ИМЯ: "))
    except:
        pass

while person.age == None:
    try:
        person.age = int(input("Введите сколько вам полных лет: "))
    except:
        pass
    
person.get_age()

p_age = person.get_age()

if p_age[-1]=='0' or p_age[-1]=='3' or p_age[-1]=='4' or p_age[-1]=='5'\
   or p_age[-1]=='6' or p_age[-1]=='7' or p_age[-1]=='' or p_age[-1]=='9':
    p_age = p_age[-1]+' лет'
    
elif p_age[-1]=='2':
    p_age = p_age[-1]+' года'
elif p_age[-1]=='1':
    p_age = p_age[-1]+' год'

print(p_age)



