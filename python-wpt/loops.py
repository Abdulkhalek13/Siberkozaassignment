# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
# Akz = Abdul khalek zouhori
people_Akz = ['lez', 'red', 'jak', 'res']

for person in people_Akz :
    print(f'current person : {person}')

#break

for person in people_Akz :
    if person == 'sara' :
        break
    print(f'current person : {person}')

# continue

for person in people_Akz :
    if person == 'sara' :
        continue
    print(f'current person : {person}')  


# range 
for i in range(len(people_Akz)):
    print(people_Akz[i])

for i in range(0 , 11):
    print(f'number : {i}')    




# While loops execute a set of statements as long as a condition is true.

count_Akz = 0
while count_Akz <= 10:
    print('count : {count_Akz}')
    count_Akz += 1