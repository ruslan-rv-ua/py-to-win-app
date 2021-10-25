import requests
from tabulate import tabulate

# docs: https://api.privatbank.ua/#p24/exchange
API_URL = "https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11"

response = requests.get(API_URL)
if response:
    print(tabulate(response.json()))
else:
    print("Error!")

input('Press <Enter> to continue')
