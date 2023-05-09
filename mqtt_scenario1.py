import paho.mqtt.client as mqtt

# Define callback functions for MQTT events
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("/esp8266/rca_room_temperature")

def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))

# Set up a MQTT client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Connect to the MQTT broker
client.connect("82.165.97.169", 1883, 60)

# Start the MQTT client loop to receive messages
client.loop_forever()
