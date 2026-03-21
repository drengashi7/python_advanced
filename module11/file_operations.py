import os
'''
file_path = "example"
file = open(file_path, "2")

content = file.read()
file.close()


    file_path = "example"

with open(file_path,"r") as file:
    content = file.read()
    print(content)
    '''

with open('example', 'r') as file:
    content = file.read() #read entire line
    line = file.readline() #read a single line
    line = file.readlines() #read all lines into a list

#writing files
with open('example', 'w') as file:
    file.write("hello world") #write data to file

lines = ["hello world!\n","welcome to python ADV!\n"]

with open('example', 'r') as file:
    file.seek(1)
    data = file.read()
    print(data)


#check if the file exists
if os.path.exists('example'):
    print("file exists")

with open('example','a') as file:
    file.write("new data appended")

#reading  adn writing in some binary data

data = b'This is some binary data'
with open ('example','rb') as binary_file:
    data = binary_file.read()


