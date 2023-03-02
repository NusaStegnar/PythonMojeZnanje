#starejsi nacin odpiranja datotek
""" f = open("test.txt", mode= "r")
data = f.read()
print(data)

f.close() """


#novejsi nacin odpiranja datotek

""" with open("test.txt", "r", encoding= "utf8") as f:
    data = f.read()
    print(data) """


""" with open("test.txt", "w", encoding= "utf8") as f:
    data = f.write("Tecaj")
    print(data) """


with open("test.txt", "a", encoding= "utf8") as f:
    data = f.write("Tecaj\n")
    print(data)