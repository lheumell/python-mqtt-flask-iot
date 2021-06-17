import sqlite3
con = sqlite3.connect('IOT.sqlite')

cur = con.cursor()

# Create table
#cur.execute('''CREATE TABLE temperature
       #        (instant text, value int, unit text)''')

# Insert a row of data
#cur.execute("INSERT INTO temperature VALUES ('2000-01-05',14.5, '°C')")
#cur.execute("INSERT INTO temperature VALUES ('2001-01-05',15.5, '°C')")
#cur.execute("INSERT INTO temperature VALUES ('2002-01-05',16.5, '°C')")
#cur.execute("INSERT INTO temperature VALUES ('2003-01-05',17.5, '°C')")

# Save (commit) the changes
con.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.

