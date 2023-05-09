import json
#true="true"
# Data to be written
x ="""[
  {
    "threadid": 11,
    "type": "inbox",
    "read": true,
    "sender": "DalYoung",
    "number": "+250783070801",
    "received": "2021-12-13 21:26:00",
    "body": "Really "
  },
  {
    "threadid": 11,
    "type": "sent",
    "read": true,
    "sender": "DalYoung",
    "number": "+250783070801",
    "received": "2021-12-13 21:26:50",
    "body": "Yeah"
  },
  {
    "threadid": 11,
    "type": "sent",
    "read": true,
    "sender": "DalYoung",
    "number": "+250783070801",
    "received": "2021-12-13 21:27:12",
    "body": "Check your WhatsApp "
  },
  {
    "threadid": 6,
    "type": "inbox",
    "read": true,
    "number": "M-Money",
    "received": "2021-12-13 21:45:17",
    "body": "You have transferred 155000 RWF to Gabriel Baziramwabo (250788862399) from your mobile money account 000600060981919 bok.bank at 2021-12-13 21:44:49. Your new balance:  . Message from sender: . Message to receiver: . Financial Transaction Id: 5453259619."
  },
  {
    "threadid": 6,
    "type": "inbox",
    "read": true,
    "number": "M-Money",
    "received": "2021-12-13 21:45:19",
    "body": "You have received 155000 RWF from Gabriel Baziramwabo (250788862399) on your mobile money account at 2021-12-13 21:44:49. Message from sender: . Your new balance:163522 RWF. Financial Transaction Id: 5453259619."
  },
  {
    "threadid": 6,
    "type": "inbox",
    "read": true,
    "number": "M-Money",
    "received": "2021-12-13 21:46:55",
    "body": "*165*S*155000 RWF transferred to Marie KAKUZE (250789494812) from 1905344 at 2021-12-13 21:46:29 .Fee was: 1500 RWF. New balance: 7022 RWF. To Buy Airtime or Bundles using MoMo, Dial *182*2*1# .*EN#"
  },
  {
    "threadid": 6,
    "type": "inbox",
    "read": true,
    "number": "M-Money",
    "received": "2021-12-14 07:22:02",
    "body": "*165*S*6000 RWF transferred to Gabriel BAZIRAMWABO (250789449645) from 1905344 at 2021-12-14 07:21:34 .Fee was: 100 RWF. New balance: 922 RWF. To Buy Airtime or Bundles using MoMo, Dial *182*2*1# .*EN#"
  },
  {
    "threadid": 6,
    "type": "inbox",
    "read": true,
    "number": "M-Money",
    "received": "2021-12-14 08:34:38",
    "body": "You have received 150000 RWF from Gabriel Baziramwabo (250788862399) on your mobile money account at 2021-12-14 08:34:11. Message from sender: . Your new balance:150922 RWF. Financial Transaction Id: 5454198628."
  },
  {
    "threadid": 6,
    "type": "inbox",
    "read": true,
    "number": "M-Money",
    "received": "2021-12-14 08:34:40",
    "body": "You have transferred 150000 RWF to Gabriel Baziramwabo (250788862399) from your mobile money account 000600060981919 bok.bank at 2021-12-14 08:34:11. Your new balance:  . Message from sender: . Message to receiver: . Financial Transaction Id: 5454198628."
  },
  {
    "threadid": 6,
    "type": "inbox",
    "read": true,
    "number": "M-Money",
    "received": "2021-12-14 08:36:15",
    "body": "*165*S*100000 RWF transferred to Egide Nsabyimana (250783500614) from 1905344 at 2021-12-14 08:35:38 .Fee was: 250 RWF. New balance: 50672 RWF. To Buy Airtime or Bundles using MoMo, Dial *182*2*1# .*EN#"
  }
]"""
      

y = json.loads(x)
for k in range(len(y)):
    print("From "+y[k]["number"]+":")
    print(y[k]["body"])
    print("")
