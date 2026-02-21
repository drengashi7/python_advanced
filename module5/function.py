#def greet():
 #   print("hello world")

#greet()

#
#def greet_person(name):
 #   print("hello", name)

#greet_person("Greta")

#def greet2(name):
    #global mesage

  #  mesage = f"hello, {name}"
 #   print(mesage)

#greet2("dreni")
#print(mesage)

#//////////////////////
#greeting = "Hello"
#name = "Uvejs"

#def greet():
    #global greeting
   # greeting = "Goodbye"

  #  name = "Dren"

 #   mesage = f"{greeting},{name} "
#    print(mesage)
#greet()

#//////////////////////////////

def greet_person(name, greeting = "Hello"):
    message = f"{greeting}, {name}"
    return message

metoda1 = greet_person("Milot")

metoda2 = greet_person("Donart", "HI")

print(metoda1)

print(metoda2)
