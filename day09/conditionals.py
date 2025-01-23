age = int(input('Enter your age: '))

if age >= 18:
	print("You are old enough to learn to drive!")
else:
	print('You need', 18 - age, 'more years to learn to drive')

my_age = 35
your_age = int(input('enter your age: '))
if your_age - my_age == 0:
	print('we are same age')
else:
	if your_age > my_age:
		print('You are', your_age - my_age, 'years older than me') if (your_age - my_age > 1) else print('You are 1 year older than me')
	else:
		print('You are', my_age - your_age, 'years younger than me') if (my_age - your_age > 1) else print('You are 1 year younger than me')

a = int(input('enter first number: '))
b = int(input('enter second number: '))
if (a > b):
	print(a, 'is greater than ', b)
elif (a < b):
	print(a, 'is less than', b)
else:
	print(a, 'equals', b)

grade = int(input('enter your score: '))

if grade < 0 or grade > 100:
	print('Not a valid grade')
elif grade < 49:
	print('Your grade is F')
elif grade > 49 and grade <= 59:
	print('Your grade is D')
elif grade > 59 and grade <= 69:
	print('Your grade is C')
elif grade > 69 and grade <= 89:
	print('Your grade is B')
else:
	print('Your grade is A')

month = input('Enter month: ').lower()
all_months = [
	'december',
	'january',
	'february',
	'march',
	'april',
	'may',
	'june',
	'july',
	'august',
	'september',
	'october',
	'november'
]
if (month == all_months[0] or month == all_months[1] or month == all_months[2]):
	print('It is Winter!')
elif(month == all_months[3] or month == all_months[4] or month == all_months[5]):
	print('It is Spring!')
elif(month == all_months[6] or month == all_months[7] or month == all_months[8]):
	print('It is Summer!')
elif(month == all_months[9] or month == all_months[10] or month == all_months[11]):
	print('It is Autumn!')
else:
	print('Month not existing')

fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input('enter a fruit: ').lower()
if fruit in fruits:
	print('That fruit already exist in the list')
else:
	fruits.append(fruit)
	print(fruits)
	
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

if ('skills' in person.keys()):
	print(person['skills'][int(len(person['skills']) / 2)])
	if 'Python' in person['skills']:
		print('has python')
	if 'React' in person['skills'] and 'Node' in person['skills'] and 'MongoDB' in person['skills']:
		print('person is Full stack dev')
	elif 'JavaScript' in person['skills'] and 'React' in person['skills']:
		print('person is frontend dev')
	elif 'Python' in person['skills'] and 'Node' in person['skills'] and 'MongoDB' in person['skills']:
		print('person is Full stack dev')
	else:
		print('unknown title')
if 'is_married' in person.keys() and 'country' in person.keys() and 'first_name' in person.keys() and 'last_name' in person.keys():
	if person['is_married'] == True and person['country'] == 'Finland':
		print(person['first_name'], person['last_name'], 'lives in', person['country'],'\b.', 'He is married.')