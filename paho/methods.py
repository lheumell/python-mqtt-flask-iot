from random import uniform
from connection import client


def mySub(salle):
    print('vous etes rentré dans la salle : ' + salle)
    client.subscribe(salle)


def myPubOnTest(salle, MSG):
    client.publish(salle, MSG)


def getTemperature():
    return round(uniform(12, 18), 2)


def salle(numeroSalle, titleSalle):
    return 'EPSI/B3A/leoH/salle' + numeroSalle + '/' + titleSalle

def disconnecting() :
    client.disconnect();
    print("Fin du programme")

