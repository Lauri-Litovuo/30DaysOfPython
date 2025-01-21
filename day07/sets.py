# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]


#Level 1

print(len(it_companies))

it_companies.add('Twitter')
print(it_companies)
it_companies.update(['Nokia', 'Xiaomi'])
print(it_companies)

it_companies.remove('Google')

try:
	it_companies.remove('raises error')
except:
	print("Raised error because not found from the set")
	

print(it_companies)

it_companies.discard('Facebook')
it_companies.discard('does nothing')
print(it_companies)

#Level 2

print(A)
print(B)
AB_joined = A.union(B)
print ('joined: ', AB_joined)

print(A.intersection(B))

print(A.issubset(B))

print(A.isdisjoint(B))

joined_A = A.union(B)
joined_B = B.union(A)

print(joined_A)
print(joined_B)

print(A.symmetric_difference(B))

del A, B, joined_A, joined_B, AB_joined

#Level 3

ages = set(age)

print(age)
print(ages)
print(len(age) - len(ages), 'ages diff because doubles are removed')

sentence = 'I am a teacher and I love to inspire and teach people'
print(len(set(sentence.split(" "))), 'words')


