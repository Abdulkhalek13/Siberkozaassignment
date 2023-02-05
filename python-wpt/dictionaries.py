# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

# Akz = Abdul khalek zouhori

# create dict

person_Akz = {
    'first_name' : 'john',
    'second_name' : 'doe',
    'age' : 33

}

# use constroctor
#person_Akz2 = dict(first_name = 'sara', last_name = 'max')

# get value

print(person_Akz['first_name'])
print(person_Akz.get('age'))

# add to dict key/value,
person_Akz['phone'] = '102030'
print(person_Akz)

# get dict keys
print(person_Akz.keys())

# get items
print(person_Akz.items())

# copy dict
person_Akz2 = person_Akz.copy()
person_Akz2['car'] = 'ford'


# removr
del(person_Akz['age'])
person_Akz.pop('phone')


#clear
person_Akz.clear

#length
print(len(person_Akz2))

#list of dicts

people = {

{'name':'mark', 'age': 15},
{'name':'jak', 'age': 20}

}
print(people[0])['name']







