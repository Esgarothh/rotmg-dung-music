import requests

#Webhook of my channel. Click on edit channel --> Webhooks --> Creates webhook   sss
mUrl = "https://discord.com/api/webhooks/839985914070433803/RUcfOIxYWSvwIVPEn09t-DcF4jcEWRofJg_NVdFue4zy3_4kvk0nvEgkCU2YZTn_vo0f"

data = {"content": 'abc'}
response = requests.post(mUrl, json=data)

print(response.status_code)

print(response.content)
