import requests

r2=requests.get('http://api.open-notify.org/astros.json')
print(r2.content)
print(r2.url)