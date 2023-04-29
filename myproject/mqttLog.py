import paho.mqtt.client as mqtt

# Callback function to handle incoming messages
def on_message(client, userdata, message):
    with open("mqtt_messages.txt", "a") as f:
        f.write(message.payload.decode() + "\n")
        print("Message written to file.")

# Create MQTT client instance
client = mqtt.Client()

# Set the callback function for incoming messages
client.on_message = on_message

# Connect to MQTT broker
client.connect("192.168.29.15", 1883, 60)

# Subscribe to the topic of interest
client.subscribe("location")

# Start the MQTT client loop
client.loop_forever()
