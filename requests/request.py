# requests module

import requests

r = requests.get("https://www.json.org/json-en.html")

#print(r.text)

with open("new/requests/json.txt","w") as f:
    f.write(r.text)


