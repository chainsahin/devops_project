import requests


api_key='16b4e873408a9cab44fcd00a'
exchange_currency=input("enter your exchange currency")
foreign_exchange_received=input("enter exchange recevied")
amount=int(input("how much money do you want to exchange:"))


api_url=f'https://v6.exchangerate-api.com/v6/{api_key}/latest/{exchange_currency}'
result=requests.get(api_url)
result=result.json()

new_amount=amount*result["conversion_rates"][foreign_exchange_received]

print(f"{amount}{exchange_currency}={new_amount:.2f}={foreign_exchange_received}")
