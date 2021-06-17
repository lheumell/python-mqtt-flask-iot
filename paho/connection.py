import paho.mqtt.client as mqtt

# Define Variables
MQTT_HOST = "test.mosquitto.org"
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 45
MQTT_TOPIC = "irisPayload"

client = mqtt.Client()

client.connect(MQTT_HOST, MQTT_PORT)
