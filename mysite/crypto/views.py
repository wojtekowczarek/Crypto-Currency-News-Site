from django.shortcuts import render

# Create your views here.
def home(request):
	import requests
	import json

	# Grab Crypto Price Data
	price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,EOS,LTC,XLM,ADA,USDT,MIOTA,TRX&tsyms=USD,EUR,JPY,PLN")
	price = json.loads(price_request.content)

	# Grab Crypto News from external API
	api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
	api = json.loads(api_request.content)
	return render(request, 'home.html', {'api': api, 'price': price})