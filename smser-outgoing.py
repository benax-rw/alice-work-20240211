import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("/outgoing_sms")

def on_message(client, userdata, msg):
    if str(msg.payload.decode()) !="[]":
        print(msg.topic+": "+str(msg.payload.decode()))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("82.165.97.169", 1883, 60)

# Start the network loop
client.loop_start()

while True:
    message = input("")
    client.publish("/incoming_sms", message)
