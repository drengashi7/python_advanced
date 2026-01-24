temperature = 96.7

name = "dren"

mosha=30

print(type(mosha))
print(type(temperature))
print(type(name))



#kalkulime

x = 8

y = 10

result = x+y

print (result)


#update values

age = 30

age+=1

print(age)

#combine values

firstName = "Dren"

last_name = "Gashi"

full_name = firstName +" "+ last_name

print(full_name)


#array (lists)

fav_colors =  ["red","green","blue","yellow","purple"]

first=fav_colors[0]
second = fav_colors[1]

print(first)
print(second)


#method for list
#append - add an item at the end of the list
fav_colors.append("orange")
print(fav_colors)

#insert - add an element in a specifik index
fav_colors.insert(2, "white")
print(fav_colors)

#remove
fav_colors.remove("blue")
del fav_colors[4]

print(fav_colors)

#update

fav_colors[0] = "pink"
print(fav_colors)