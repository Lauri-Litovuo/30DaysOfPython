dog = dict()

dog = {'name': 'Mauno', 'color':'whitebrown', 'breed':'french bulldog', 'legs':4, 'age':10}
print(dog)

student = {
	'first_name':'Lauri',
	'last_name': 'Litovuo',
	'gender':'male',
	'age':35,
	'marital status':False,
	'skills':['C', 'Cpp', 'python'],
	'country':'Finland',
	'city':'Helsinki',
	'address':'kallio'
}

print(len(student))

print(student.get('skills'), type(student.get('skills')))

student['skills'].append('data analytics')
student['skills'].append('git')
print(student)

print(student.keys())
print(student.values())
print(student.items())
del student['city']
student.popitem() # removes the last item
student.pop('gender')

print(student)

del dog