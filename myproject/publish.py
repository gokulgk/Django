import paho.mqtt.client as mqtt

# MQTT broker configuration
BROKER_ADDRESS = "192.168.110.132"
BROKER_PORT = 1883
TOPIC = "interrupt"

# Create an MQTT client instance
client = mqtt.Client()

# Connect to the MQTT broker
client.connect(BROKER_ADDRESS, BROKER_PORT)

# Publish a message to the specified topic
message = str(1)
client.publish(TOPIC, message)
client.loop()
# Disconnect from the MQTT broker
client.disconnect()
