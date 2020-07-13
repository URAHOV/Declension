## В.13 з.1. Написать программу, которая после введенного с клавиатуры возраста человека,
## дописывала бы слово «год» в правильной форме. Напр: 3 года, 21 год, 45 лет.
## Если число оканчивается на 1, то "год".
## Если на 2,3,4, то "года". Если на 0,5,6,7,8,9, то "лет".

# явное лучше неявного
from classes import Person

person = Person()

while person.name == '':
    try:
        person.name = str(input("ВВЕДИТЕ СВОЁ ИМЯ: "))
        p_name = person.name
    except:
        pass

while person.age == None:
    try:
        person.age = int(input("Введите сколько вам полных лет: "))
    except:
        pass

p_age = person.get_age()

if len(p_age)==2 and p_age in ['11','12','13','14']:
    years = 'лет'    
elif p_age[-1] in ['0','5','6','7','8','9']:
    years = 'лет' 
elif p_age[-1] in ['2','3','4']:
    years = 'года' 
elif p_age[-1]=='1':
    years = 'год'

print(f"Ваше имя: {p_name} и вам {p_age} {years}")
