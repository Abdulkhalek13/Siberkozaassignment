# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 # Akz = Abdul khalek zouhori
  
 # create tuple
fruit_Akz = ('Apple','orange','grapes')
# fruit_Akz2 = tuple(('Apple','orange','grapes'))
# single value needs trailing comma
fruit_Akz2 = ('Apple',)

print(fruit_Akz[0])
# tuple values can't be changed (not like lists)
#print(fruit_Akz2 , fruit_Akz ,type(fruit_Akz2))

# delete tuple 
del fruit_Akz2

print(len(fruit_Akz))



# A Set is a collection which is unordered and unindexed. No duplicate members.

# creat set

cars_Akz = {'ford', 'gmc' , 'cad'}

print(cars_Akz , type(cars_Akz))

# chek if in set
print('ford' in cars_Akz)

# add to the set
cars_Akz.add('chevo')
print(cars_Akz)

# remove from set
cars_Akz.remove('chevo')

print(cars_Akz)

# clear set
cars_Akz.clear()
print(cars_Akz)















