#vaja

import random

number = random.randint(1, 50)
while True:
   ugib = int(input("Vnesi stevilo: "))
   if ugib < number:
    print("Premajhno... ")
   elif ugib > number:
    print("Preveliko... ")
   else:
    print("Bravo")
    break
