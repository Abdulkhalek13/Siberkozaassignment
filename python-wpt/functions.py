# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces

# Akz = Abdul khalek zouhori

#create function

def sayhello_Akz(name):
    print(f'hello {name}')
    sayhello_Akz('masha')

# return val
def getsum_Akz(num1 , num2):
    total = num1 + num2
    return total

print(getsum_Akz(1,2))

num = getsum_Akz(3,5)



# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

getsum_Akz = lambda num1, num2 : num1 + num2
print(getsum_Akz(1,10))









