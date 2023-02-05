# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Akz = Abdul khalek zouhori

# creat class

class User_Akz:
    #constructor
    def __init__(self, name , email , age):
        self.name = name
        self.email = email
        self.age = age

    def greeting_Akz(self):
     return f'my name is {self.name} and i am {self.age}'

    def has_birthday_Akz(self):
        self.age +=1
         


# extend class 
class Customer_Akz (User_Akz):
    #constructor
    def __init__(self, name , email , age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def setbalance_Akz(self , balance):
        self.balance = balance  

    def greeting_Akz(self):
     return f'my name is {self.name} and i am {self.age} and balance is {self.balance}'


# init user object

brad = User_Akz('brad' , 'brademail.com', 20)
print(type(brad))

brad.has_birthday_Akz()

print(brad.greeting_Akz())

# init customer object
janeat = Customer_Akz('janeat' , 'janeat.com', 20 )
janeat.setbalance_Akz(500)
print(janeat.greeting_Akz())



