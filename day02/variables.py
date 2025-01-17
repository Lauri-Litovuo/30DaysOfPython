#Day 2: 30 Days of Python programming

#Exercise 1

first_name = 'Lauri'
last_name = 'Litovuo'
full_name = 'Lauri Litovuo'
country = 'Finland'
city = 'Helsinki'
age = 35
year = 2025
is_married = False
is_true = True
is_light_on = True

multiple, variables, on, one, line = 1, 2, 'three', 'four' , True

print(first_name)
print(type(first_name))
print(len(first_name))
print('comparing lenght of first and last name: ', abs(len(first_name) - len(last_name)), 'letters')
num_one, num_two = 5 , 4
total = sum([num_two, num_one])
diff = num_two - num_one
product = num_one * num_two
division = num_two / num_one
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two
print (num_one, num_two, total, diff, product, division, remainder, exp, floor_division)

import math

radius = 30
area_of_circle = math.pi * (radius ** 2)
print(area_of_circle)
circum_of_circle = 2 * math.pi * radius
print(circum_of_circle)

radius = int(input('write radius: '))
area_of_circle = math.pi * (radius ** 2)
print('area of the circle is:  ', area_of_circle)
circum_of_circle = 2 * math.pi * radius
print('circum of the circle is:', circum_of_circle)

first_name = input('what is your first name: ')
last_name = input('What is your last name: ')
country = input('where are your from: ')
age = int(input('how old are you: '))

print('hello', first_name, last_name, age, country)

