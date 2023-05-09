import json
y=json.dumps(['foo', {
      'bar': ('baz', None, 1.0, 2)
   }])
print(y)
n=json.loads(y)
print(n[0]["bar"])
