#vaja za izpis razdalje med kraji

import requests

'''

kraj1 = str(input("Vnesi prvi kraj"))
#kraj2 = str(input("Vnesi drugi kraj"))

x = kraj1
#y = kraj2

url = ("https://jsonplaceholder.typicode.com/posts/%s" %(x))
#print(url)

razdalja = requests.get(url)
razdalja_decoded = razdalja.json()
#print(razdalja_decoded)

kilometri = razdalja_decoded["body"] #[0]["distance"]["text"]
print("b: " + kilometri)
#print("Med krajem" , kraj1 "in krajem" , kraj2 , "je" , kilometri)
'''

