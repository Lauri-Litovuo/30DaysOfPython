# age = 35
# height = 1.83
# complx = 1 + 3j

# base = input('enter base: ')
# triangle_height = input('enter height: ')

# area = 0.5 * int(base) * int(triangle_height)
# print('The area of the triangle is', area)

# side_a = input('input side a: ')
# side_b = input('input side b: ')
# side_c = input('input side c: ')

# perimeter = int(side_a) + int(side_b) + int(side_c)
# print('The perimeter of the triangle is', perimeter)

# rect_lenght = int(input('input lenght: '))
# rect_width = int(input('enter widht: '))

# rect_area = 2 *(rect_lenght + rect_width)
# print('rectangle area is', rect_area)

# radius = int(input('enter radius: '))
# circ_area = 3.14 * (radius ** 2)
# circ_circum = 2 * 3.14 * radius

# x1, y1, x2, y2 = 2, 2, 6, 10
# slope = (y2- y1)/(x2 - x1)
# print(slope)

# print ('comparing', int(slope - 2))

# import math
# print(math.sqrt((x2-x1)**2 + (y2-y1)**2))

# y_intercept = 2 * 0 - 2
# x_intercept = (0 + 2) / 2

# print ('x and y intercept ex08:', x_intercept, y_intercept)

x = -3

y = (x ** 2) + (6 * x) + 9
print (y)

str1 = 'python'
str2 = 'dragon'

print ('lenghts of python and dragon', len(str1), len(str2))
print('False statement', bool(str1 == str2))

print ('is in sentence?: ', bool('jargon' in 'I hope this course is not full of jargon.'))
print ('is on on dragon and python: ', 'on' in str1, 'on' in str2)
conversion = str(float(len('python')))
print(conversion, type(conversion))

num = 3
if (num % 2 == 0):
	print(num, 'is even')
else:
	print(num, 'not even')

print(bool(7 // 3 == int(2.7)))

print(bool(type('10') == type(10)))

print(bool(int(float('9.8')) == 10))

hours = input('enter hours: ')
rate = input('enter rate: ')

pay = int(hours) * int(rate)
print('your pay is', pay)

years = input('enter years: ')
seconds = int(years) * 31536000
print('you have lived for', seconds, 'seconds')

i = 1
while (i <= 5):
	print (i, 1, i, i * i, i ** 3)
	i += 1
