import requests

#http://api.open-notify.org/astros.json



astronavti = requests.get("http://api.open-notify.org/astros.json")
astronavti_decoded = astronavti.json()
#print(astronavti_decoded)

stevilo_ast = astronavti_decoded["number"]
print("Trenutno je v vesolju: ", stevilo_ast , "astronavtov")
print("Imena astronavtov: ")

for astronavt in astronavti_decoded["people"]:
    print(astronavt["name"])



