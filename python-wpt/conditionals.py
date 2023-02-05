# If/ Else conditions are used to decide to do something based on something being true or false

# Akz = Abdul khalek zouhori

x_Akz = 10
y_Akz = 5



# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values

#if x_Akz > y_Akz :
  #  print('{x_Akz} is greater then {y_Akz}')

# if / else

#if x_Akz > y_Akz :
   # print('{x_Akz} is greater then {y_Akz}')
#else:
   # print('{y_Akz} is greater then {x_Akz}')

# elif

if x_Akz > y_Akz :
   print('{x_Akz} is greater then {y_Akz}')
elif y_Akz > x_Akz:
    print('{y_Akz} is greater then {x_Akz}')

# if nested
if x_Akz > 2 :
    if x_Akz < 10:
        print('{x_Akz} is greator then 2 and less or equal to 10')

# Logical operators (and, or, not) - Used to combine conditional statements

if x_Akz > 2 and x_Akz <= 10 :
    print('{x_Akz} is greator then 2 and less or equal to 10')

if x_Akz > 2 or x_Akz <= 10 :
    print('{x_Akz} is greator then 2 and less or equal to 10')

if not(x_Akz==y_Akz):
    print(f'{x_Akz} is not equal to {y_Akz}')



# Membership Operators (in, not in) - Membership operators are used to test if a sequence is presented in an object

numbers_Akz = [1, 2, 3 ,4 ,5]
if x_Akz in numbers_Akz :
    print(x_Akz in numbers_Akz)

elif x_Akz not in numbers_Akz :
    print(x_Akz not in numbers_Akz)


# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:


if x_Akz is y_Akz:
    print(x_Akz is y_Akz)
else :
    print(x_Akz is not y_Akz)
