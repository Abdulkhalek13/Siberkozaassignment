# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

#Akz = Abdu khakek zouhori

name_Akz = 'brad'
age_Akz = 37

# concatenate
#age = str(age)

print('hello my name is ' + name_Akz +' i am ' + str(age_Akz ))

# String Formatting
# Arguments by position
print('my name is {name_Akz}  and i am {age_Akz}'.format(name_Akz=name_Akz, age_Akz = age_Akz))
# F-strings 
print(f'heloo my name is {name_Akz} and i am {age_Akz}')

# String Methods 
s_Akz = 'hello python'
# capitalize string
print(s_Akz.capitalize())
# make all uppercase
print(s_Akz.upper())
# swap case
print(s_Akz.swapcase())
# get length
print(len(s_Akz))
# replace
print(s_Akz.replace('python','world'))
# count
L_Akz = 'l'
print(s_Akz.count(L_Akz))
#start with
print(s_Akz.startswith('hello'))
#ends with
print(s_Akz.endswith('n'))
#split into  a list
print(s_Akz.split())
#find pos
print(s_Akz.find('t'))
# is all alphanumaric
print(s_Akz.isalnum())
# is all alphabic
print(s_Akz.isalpha())
#is all numaric
print(s_Akz.isalnum())




















