import json

x = b'[{"id": "001","question": "How did you find the IP address of the device you are logged into now?"  },  {"id": "002","question": "What is the MAC address of the device you are logged into now?"  },  {"id": "003","question": "What is the IPv4 address of the device you are logged into now?"  },     {"id": "004","question": "Which command have you used to log into this device?"  },   {"id": "005","question": "Is this device connected to the internet? If yes how did you know it?"  },  {"id": "006","question": "What is the default gateway of this device you are logged into?"  },   {"id": "007","question": "How does NAT operate on the network of Rwanda Coding Academy? What is public IP does NAT is giving the device you are logged into now?"  },      {"id": "008","question": "How many devices have currently the port 80 open on the network you are connected to?"  },   {"id": "009","question": "How can users benefit from using FTP? [In 10 words at most]"  },      {"id": "010","question": "In which case using SMTP from the terminal can serve us most? [In 10 words at most]"  }]'

y = json.loads(x)


for k in range(len(y)):
    print("Question-"+y[k]["id"]+":")
    print(y[k]["question"])

