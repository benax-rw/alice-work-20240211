import json,urllib.request

x = urllib.request.urlopen("https://secure.benax.rw/testJson.json").read()
y = json.loads(x)

for k in range(len(y)):
    print(y[k]["id"])
    print(y[k]["question"])
