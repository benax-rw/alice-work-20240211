import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect("82.165.97.169", 1883, 60)

# Start the network loop
client.loop_start()

while True:
    message = input("")
    client.publish("/light_switching", message)
