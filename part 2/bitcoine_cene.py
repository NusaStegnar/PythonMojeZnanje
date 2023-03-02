import requests
import time
import datetime

url = 'https://rest.coinapi.io/v1/exchangerate/BTC/USD'
headers = {'X-CoinAPI-Key' : 'C56DC94B-C79D-45D7-A6D5-13C83BC90B07'}

def pridobi_cene():
    response = requests.get(url, headers=headers)
    data = response.txt
    data = response.json()
    rate = data["rate"]
    print(rate)    
    return rate


while True:
    rate = pridobi_cene
    with open("cene.txt", "a") as f:
        f.write(f"Zadnja_cena = {rate} \n")

    time.sleep(2)
