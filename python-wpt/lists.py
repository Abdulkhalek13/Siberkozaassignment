# A List is a collection which is ordered and changeable. Allows duplicate members.
# Akz = Abdul khalek zouhori
numbeers_Akz = [1, 2, 3, 4, 5]
fruits_Akz = ['apple', 'oranges' , 'grapes' , 'pears']

# use a constructor
numbeers2_Akz = list((1, 2, 3, 4, 5))
print(numbeers_Akz , numbeers2_Akz)

# get a value
print(fruits_Akz[2])

# get a length
print(len(fruits_Akz))

# append to list or insert into it
fruits_Akz.append('mango')
print(fruits_Akz)

fruits_Akz.insert(3, 'banana')


# remove from a list and from a pos with pop
fruits_Akz.remove('apple')
print(fruits_Akz)

fruits_Akz.pop(4)
print(fruits_Akz)

# revers list
fruits_Akz.reverse()
print(fruits_Akz)

# sort list
fruits_Akz.sort()
print(fruits_Akz)

#reverse sort
fruits_Akz.sort(reverse= True)

# change value
fruits_Akz[0] = 'blueberries'
print(fruits_Akz)



















