import json,urllib.request

data = {
'network': u'MTN RWANDA',
'msisdn': '250785971082',
'timestamp': '2021-10-22T16:51:53.662295+0200', 'newrequest': 1,
'mccmnc': u'65533',
'sessionid': u'2a68a04d-7fa9-4bc1-8612-b62fe7dc04fa', 'serviceid': u'128a6f05-9ee1-46c7-a216-49acb1a501c232', 'entrypoint': u'*559*1#',
'input': '559*1',
'transactionid': u'c19c1c7f-002a-4740-aebb-95382b6f0392', 'customerid': u'630e5f31-0bc3-4420-8f41-01bea8c69f5322'
}
r = requests.post(url,json=data,headers=={'content-type':"application/json"},verify=False)

print(r. r.json(), r.status_code)
