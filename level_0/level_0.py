#!/usr/bin/python
import requests
s = requests.Session()
url = "http://158.69.76.135/level0.php"

s.get(url)

headers = {
  'Referer' : 'http://158.69.76.135/level0.php'
}

data = {
  'id': '1033',
  'holdthedoor': 'Valider'
}
i = 0
while i < 1024:
  s.post('http://158.69.76.135/level0.php', headers=headers, data=data)
  i += 1
