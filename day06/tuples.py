#ex01

tpl = tuple()
print(tpl)

sisters = ('sister_one', 'sister_two')
brothers = ('bother_one', 'brother_two')

siblings = sisters + brothers

print(siblings, len(siblings))

siblings = list(siblings)
siblings += ['father', 'mother']

siblings = tuple(siblings)
print(siblings)

family_members = siblings
print(family_members)

#ex02

siblings = family_members[:4]
parents = family_members[-2:]
print (siblings)
print(parents)

fruits = ('orange', 'mango')
vegetables = ('cucumber', 'carrot')
animal_products = ('milk', 'eggs')

food_stuff_tp = fruits + vegetables + animal_products

food_stuff_lt = list(food_stuff_tp)
print(food_stuff_tp)
print(food_stuff_lt)

middle_items = food_stuff_tp[1:-1]
print(middle_items)

front_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]

print(front_three)
print(last_three)

del food_stuff_tp
#print(food_stuff_tp)

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)





