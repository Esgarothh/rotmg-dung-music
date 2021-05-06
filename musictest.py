import requests

#Webhook of my channel. Click on edit channel --> Webhooks --> Creates webhook   sss
mUrl = "https://discord.com/api/webhooks/729017161942******/-CC0BNUXXyrSLF1UxjHMwuHA141wG-FjyOSDq2Lgt*******************"

data = {"content": 'abc'}
response = requests.post(mUrl, json=data)

print(response.status_code)

print(response.content)
