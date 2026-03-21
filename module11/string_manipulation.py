with open('example','r') as file:
    for line in file:
        cleaned_line = line.strip()
        print(cleaned_line)

with open ('example', 'r') as file:
    for line in file:
        words = line.strip().split()
        print(words)

#contatenating strings

name = 'alice'
age = 30

with open ('output','w') as file:
    file.write(f"name:{name}\n")
    file.write(f"age: {age}\n")

with open('example','r') as file:
    for line in file:
        cleaned_line = line.strip()
        modified_line = cleaned_line.replace("line_1","line_x")
        






