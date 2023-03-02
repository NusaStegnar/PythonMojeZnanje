'''
print(1)
print(2)
print(3)

#...
print(99)
print(100)


number = 1
while number < 101:
    print(number)
    #number = number + 1
    number += 1


number = 100
while number < 501:
    print(number)
    number += 1



#for zanka

items = [1, 2, 3, 4, 5]
for item in items:
    print(item)
for i in range (9):
    print (i + 1)


items =  ["jabolka", "banane", "ananas"]
for sadje in items:
    print(sadje)


for n in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print("2 na", str(n), "je", str(2**n))


for n in [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]:
    print("5 na" , str(n), "je", str(5**n))


#continue

item = ["banane", "jabolka", "ananas"]
for sadje in item:
    if sadje == "jabolka":
        continue
    print(sadje)


#break

items = ["banane", "jabolka", "ananas"]
for sadje in items:
    if sadje == "jabolka":
        break
    print(sadje)

number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for n in number:
    if n == 7:
        continue
    print(n)

'''

number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for n in number:
    if n == 7:
        break
    print(n)
