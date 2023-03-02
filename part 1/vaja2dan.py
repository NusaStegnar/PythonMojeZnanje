import random
'''
number = random.randint(1, 101)
while True:
    ugib = int(input("Insert number: "))
    if ugib > number:
        print("The number you are looking for is smaller")
    elif ugib < number: 
        print("The number you are looking for is biger")
    else:
        print("Bravo, you guessed it")
        break

'''

#druga verzija

ponovitve = 0
print("What is yur name")

user = input()
number = random.randint(1, 20)
print("Try it")

while ponovitve < 6:
    poskus = input()
    poskus = int(poskus)
    ponovitve += 1

    if poskus < number:
        print("Premalo ...")

    if poskus > number:
        print("Prevec")

    if poskus == number:
        break

if poskus == number:
    ponovitve = str(ponovitve)
    print("Bravo, " + user + ". Uganil si v " + ponovitve + " poskusih!")

if poskus != number:
    number = str(number)
    print("Zal... stevilo, na katerega smo mislili, je bilo" + number)

 