
strings = ['Thirty', 'Days', 'Of', 'Python']

print(" ".join(strings))

print(" ".join(['Coding', 'For', 'All']))

company = 'Coding For All'
print(company)
print(len(company))
print(company.upper())
print(company.lower())

print(company.capitalize())
print(company.title())
print(company.swapcase())
print(company[company.index(" "):])

print(bool(company.find("Coding") != -1))

print(('Coding For All').replace('Coding', 'Python'))

print(('Python for Everyone').replace('Everyone', 'All'))

print(company.split(' '))

print(('Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon').split(','))

print(company[0])

print(company[-1])

print(company.index('F'))

print(('Coding For All People').rfind('l'))

sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))
print(sentence.rfind('because'))

print(sentence[0:sentence.find('because')] + sentence[sentence.rfind('because') + len('because'):])

print(bool(('Coding For All').find('Coding') != -1))

print(company.endswith('coding'))

print('  Coding For All  '.strip(' '))

if ('30DaysOfPython'.isidentifier() == True):
	print('30DaysOfPython is valid')
elif ('thirty_days_of_python'.isidentifier() == True):
	print('thirty_days_of_python is valid')

print('# '.join(['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']))
print('I am enjoying this challenge.\nI just wonder what is next.')
print('Name\t\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki')

radius = 10
area = 3.14 * radius ** 2

print('radius = {}\narea = 3.14 * radius ** 2\nThe area of circle with radius {} is {} meters square.'.format(radius, radius, int(area)))

first_num = 8
second_num = 6

print(f'{first_num} + {second_num} = {first_num + second_num}')
print(f'{first_num} - {second_num} = {first_num - second_num}')
print(f'{first_num} * {second_num} = {first_num * second_num}')
print(f'{first_num} / {second_num} = {(first_num / second_num):.2f}')
print(f'{first_num} % {second_num} = {first_num % second_num}')
print(f'{first_num} // {second_num} = {first_num // second_num}')
print(f'{first_num} ** {second_num} = {first_num ** second_num}')

