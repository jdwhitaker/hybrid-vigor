import urllib.parse

with open('names.txt', 'r') as f:
    names = f.readlines()

for name in names:
    name = name.strip()
    path = "/query/{}".format(urllib.parse.quote(name))
    print(path)
