# modules in python
import math
import os
import mymodule
import requests

print(math.sqrt(2))
mymodule.hello()
r = requests.get("https://docs.python.org/3/py-modindex.html")
print(r.text)