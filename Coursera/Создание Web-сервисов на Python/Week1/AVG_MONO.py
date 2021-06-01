import re

import requests

result = requests.get('https://finance.i.ua/')
html = result.text

match = re.search(r'115.*?EUR\D+buy\D+(\d+.\d+)', html)
EUR_buy_mono = re.findall(r'115.*?EUR\D+buy\D+(\d+.\d+)', html)
EUR_sell_mono = re.findall(r'115.*?EUR.*?sell\D+(\d+.\d+)', html)
USD_buy_mono = re.findall(r'115.*?USD\D+buy\D+(\d+.\d+)', html)
USD_sell_mono = re.findall(r'115.*?USD.*?sell\D+(\d+.\d+)', html)
avg_USD_mono = ((float(USD_buy_mono[0]))+(float(USD_sell_mono[0])))/2
avg_EUR_mono = ((float(EUR_buy_mono[0]))+(float(EUR_sell_mono[0])))/2
print('avg_USD_mono - ', round(avg_USD_mono, 2))
print('avg_EUR_mono - ', round(avg_EUR_mono, 2))

