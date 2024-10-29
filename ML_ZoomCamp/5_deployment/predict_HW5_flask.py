
import requests


url = 'http://127.0.0.1:9696/subscription'

customer_id = 'client'
client = {"job": "management", "duration": 400, "poutcome": "success"}


response = requests.post(url, json=client).json()

print(response)

# print('probability that this client will get a subscription now %s' %(response[1]))




