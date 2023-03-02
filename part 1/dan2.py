import math as m

#vaja1
#print(m.sqrt(45))
#print(m.sqrt(225))
#print(m.sqrt(51023))
#print(m.sqrt(442))

#vaja2

#user = input("Insert your name: ")
#age = input("Insert your age: ")

#print("Hello " + user + ", ki je star " + age + " let!")

#user = input("Insert your name and surname: ")
#age = input("Insert yur age: ")
#address = input("Insert your address: ")

#print("Hello " + user + ", star " + age + " , iz " + address)

#vaja3

#age = int(input("Insert your age: "))

#print(age > 18)
#print(age < 18)

#color = input ("Insert the color of your eyes: ")
#a = ("blue")
#b = ("green")
#c = ("grey")

#print(color == a)
#print(color != a)

#vaja4

#number1 = int(input("Insert first number: "))
#number2 = int(input("Insert second number: "))
#number3 = int(input("Insert third number: "))

#print(number1 + number3 + number2)
#print(number1 + number3 - number2)
#print(number1 * number3 / number2)
#print(number1 - number3 * number2)
#print(number1 / number3 + number2)
#print(number1 / number3 / number2)
#print(number1 * number3 + number2)


user = input("Insert your name: ")
genderUserInput = input("Insert your gender: (M/F) ")

genderNormalized = genderUserInput.lower()

print("No. of chars: " + str(len(user)))

if genderNormalized == "m": 
    print(f"Hello, {user}!")
elif genderNormalized == "f":
    print (f"Hi, {user}!")
else:
    print(f"Hello, {user}, tega spola '{genderUserInput}', ne podpiramo")

