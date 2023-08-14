import urllib.parse
import random

for i in range(1,101):
    path = "/query/{i}".format(urllib.parse.quote(i))
    print(path)
