import sqlite3

import paho.mqtt.client as mqtt
import json
from initBdd import cur


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("EPSI/B3A/leoH/salle2/temperature")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    obj = json.loads(msg.payload)
    myValue = obj["value"]
    myInstant = obj["instant"]
    myUnit = obj["unit"]
    con = sqlite3.connect('IOT.sqlite')

    cur = con.cursor()
    print(myValue)
    cur.execute("INSERT INTO temperature VALUES (?, ?, ?)",
                (myInstant, myValue, myUnit))
    con.commit()


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitto.org", 1883, 60)
client.loop_forever()
