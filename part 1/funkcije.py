'''
#primer fibonachi

def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a+b
    print()

fib(50)
fib(30)



#primer imena

def say_hello(name = "Stranger"):
    print("Hello %s!" %name)

say_hello("Nusa")
say_hello("Peter")


def say_hello(name = 'Stranger'):
    return "Hello %s!" %name

print(say_hello("Nusa")) 

nusa = say_hello("Nusa")
print(nusa)



string = str(input("Napisi neko besedilo: "))
locilo = str(input("Dodaj se klicaj"))

def blabla():
    print(string + locilo)

if locilo == "!":
    print ("Pohvalno")

else:
    print("Ne ves kaj je klicaj... sramota")

'''

a = [1, 2, 3, 4]
b = [5, 6, 7, 8, 9]
c = [10, 11, 12, 13, 14, 15]

def povprecje(seznam):
    return sum(seznam) / len(seznam)

print(povprecje(a))
print(povprecje(b))
print(povprecje(c))