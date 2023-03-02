#user input

#user = input("What is your name: ")

#print(f"Hello, {user}")
#print("Hello, " + user)

#If/elif/else

user = input("Insert your name? ")
gender = input ("Insert your gender (M/F)? ")

if gender == "M":
    print(f"Hello, {user}!")
elif gender == "F":
    print(f"Hi, {user}!")
else:
    print(f"{user}, tega spola '{gender}' ne podpiramo! ")


#pass

user = input("Insert your name: ")

if len(user) < 4:
    pass
#NE POZABI IMPLEMETIRATI FUNKCIJE/KODE

print("End of program")