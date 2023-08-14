import os
import sqlite3
import random

with open('names.txt', 'r') as f:
    names = f.readlines()

data = [(name.strip(), random.randint(1,100)) for name in names]

# set up data
try: os.remove('web.db')
except: pass
con = sqlite3.connect("web.db")
cur = con.cursor()
cur.execute("CREATE TABLE users(name,favorite_number)")
cur.executemany("INSERT INTO users VALUES(?,?)", data)
con.commit()
con.close()
