# Python has functions for creating, reading, updating, and deleting files.

# Akz = Abdul khalek zouhori

# open a file
myfile_Akz = open('myfile.txt' , 'w')

# get some info
print('Name' , myfile_Akz.name)
print('is closed' , myfile_Akz.closed)
print('opening mode' , myfile_Akz.mode)

# write to file
myfile_Akz.write('my name is :')
myfile_Akz.write('abdul khalek')
myfile_Akz.close()

# add to file
myfile_Akz = open('myfile.txt' , 'a')

myfile_Akz.write('my name age :')
myfile_Akz.write('30')
myfile_Akz.close()


# read from file
myfile_Akz = open('myfile.txt' , 'r')
text = myfile_Akz.read(100)
print(text)


