import json
import methods
from time import sleep, strftime, gmtime

import temperature

numeroSalle = "2"
titleSalle = "temperature"

methods.mySub(methods.salle(numeroSalle, titleSalle))

i = 0
while i < 100:
    temperature.data["value"] = methods.getTemperature()
    temperature.data["instant"] = strftime("%a, %d %b %Y %I:%M:%S %p %Z", gmtime())
    MQTT_MSG = json.dumps(temperature.data)
    methods.myPubOnTest(methods.salle(numeroSalle, titleSalle), MQTT_MSG)
    i += 1
    sleep(2)

methods.disconnecting()



#mosquitto_sub -h test.mosquitto.org -p 1883 -t EPSI/B3A/leoH/salle1/temperature

