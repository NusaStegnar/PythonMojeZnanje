
#https://api.sunrise-sunset.org/json?lat=%s&lng=%s

import requests

'''
fact = str(input("Zanimiva dejstva: "))
url_fact = ("http://api.fungenerators.com/fact/random?category=Countries&subcategory=USA")

#print(url_fact)

dejstva = requests.get(url_fact)
dejstva_decoded = dejstva.json()
print(dejstva_decoded)

'''











#print("Spremljal bos vzhod in zahod")

url_zahod = ("https://api.sunrise-sunset.org/json?lat=%s&lng=%s" %s(prvi_lat, prvi_long))

podatki_zahod = requests.get(url_zahod)
podatki_zahod_decoded = podatki_zahod.json()

print(podatki_zahod_decoded)