lst = list()
print(lst)

lst = ['one', 'two', 'three', 'four', 'five']
print(lst)
print(len(lst))

print(lst[0], lst[int(len(lst) / 2)], lst[-1])

mixed_data_types = ['Lauri', 35, 1.83, False, 'Helsinki']
print(mixed_data_types)

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)

print(len(it_companies))

print(it_companies[0], it_companies[int(len(it_companies) / 2)], it_companies[-1])

it_companies[0] = 'Nokia'
print(it_companies)

it_companies.append('Facebook')
print(it_companies)

it_companies.insert(2, 'Xiaomi')
print(it_companies)

it_companies.insert(int(len(it_companies) / 2,), 'Uber')
print(it_companies)

it_companies[0] = it_companies[0].upper()
print(it_companies)

print('#; '.join(it_companies))

print('Uber' in it_companies)
print('Tesla' in it_companies)

it_companies.sort()
print(it_companies)

it_companies.reverse()
print(it_companies)

shorted_list = it_companies[:3]
print(shorted_list)


shorted_list = it_companies[-3:]
print(shorted_list)

shorted_list = it_companies[int(len(it_companies) / 2)]
print(shorted_list)

print(it_companies)
it_companies.pop(0)
print(it_companies)

it_companies.pop(int(len(it_companies) / 2))
print(it_companies)

it_companies.pop()
print(it_companies)

it_companies.clear()
print(it_companies)

del it_companies
#print(it_companies)

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

joined_ends = front_end + back_end
print(joined_ends)

full_stack = joined_ends.copy()

full_stack[full_stack.index('Redux') + 1:full_stack.index('Redux') + 1] = ['Python', 'SQL']
print(full_stack)


#Level 2

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
print(ages)
ages.sort()
print(ages)
print(ages[0])
print(ages[-1])

print(ages[int(len(ages) / 2)])

print(sum(ages[:]) / len(ages))

print(ages[-1] - ages[0])

print(abs(ages[0]-sum(ages[:]) / len(ages)), abs(ages[-1]-sum(ages[:]) / len(ages)))

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]

print(countries[int(len(countries) / 2)])

if (len(countries) % 2 == 0):
	first_half = countries[:int(len(countries) / 2)]
	second_half = countries[int(len(countries) / 2):]
else:
	first_half = countries[:int(len(countries) / 2) + 1]
	second_half = countries[int(len(countries) / 2) + 1:]

print(first_half, len(first_half))
print(second_half, len(second_half))
print(len(countries), len(first_half) + len(second_half))

selected_countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first, second, third, *nordic = selected_countries

print(first)
print(second)
print(third)
print(nordic)

