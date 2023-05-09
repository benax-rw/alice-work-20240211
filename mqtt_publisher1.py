import paho.mqtt.client as mqtt

# Create a new MQTT client instance
client = mqtt.Client()

# Connect to a broker
client.connect("82.165.97.169", 1883)

# Start the network loop
client.loop_start()
while True:
	# Publish a message to a topic
	client.publish("/mytopic", "Hello from Gabriel")

# Stop the network loops
client.loop_stop()

# Disconnect from the broker
client.disconnect()
