import sqlite3


def temperatures():
    con = sqlite3.connect("../BDD/IOT.sqlite")
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute("select * from temperature")
    return cur.fetchall();


def temperaturesValue():
    data = []
    con = sqlite3.connect("../BDD/IOT.sqlite")
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute("select value from temperature")
    rows = cur.fetchall();

    for row in rows:
        data.append(list(row))
    return data

def temperaturesInstant():
    data = []
    con = sqlite3.connect("../BDD/IOT.sqlite")
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute("select instant from temperature")
    rows = cur.fetchall();

    for row in rows:
        data.append(list(row))
    return data
