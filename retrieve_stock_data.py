# -*- coding: utf-8 -*-
"""retrieve-stock-data.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17QsfLqiObdfNWFeuBcLHp6RUzcYv3MYA

Stock Data API

Q: Is there and how long is the delay?

Docs:
* https://iextrading.com/developer/docs/#chart
  Chart request: https://api.iextrading.com/1.0/stock/[TICKER]/chart/1m OR 1d etc

Also see:
* https://iextrading.com/developer/docs/#peers
"""

import requests

#@title Stock Search
ticker = "fb" #@param {type:"string"}
timeline = "1m" #@param ["1d", "1m", "3m"]

# Request URL
url = 'https://api.iextrading.com/1.0/stock/%s/chart/%s' % (ticker, timeline)

r = requests.get(url)

j = r.json()

# Preview data
print(json.dumps(j, indent=3)[:500])

# Arrays of variables
date = []
high = []
low = []
vol = []

for t in j:
  date.append(t.get("label"))
  high.append(t.get("high"))
  low.append(t.get("low"))
  vol.append(t.get("volume"))
  
data = [date, high, low, vol]

csv = ''

for V in data:
  for v in V:
    if ',' in str(v):
      csv += '\"%s\",' % v
    else:
      csv += '%s,' % str(v)
  csv += '\n'

  
print(csv)

