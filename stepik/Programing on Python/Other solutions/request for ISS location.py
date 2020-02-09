import requests

parameters = {"lat": 54.43, "lon": 20.30,"n":5}
r1 = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
print(*r1.content)