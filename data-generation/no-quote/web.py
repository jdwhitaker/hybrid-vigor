import sqlite3
from flask import Flask, request
import logging

logging.basicConfig(filename='malicious.log',level=logging.DEBUG)

app = Flask(__name__)

@app.route("/query/<number>")
def query(number):
    app.logger.debug(request.path)
    con = sqlite3.connect("web.db")
    cur = con.cursor()
    res = cur.execute(f"SELECT name FROM users WHERE favorite_number={number}")
    names = res.fetchall()
    names = ','.join([i[0] for i in names])
    return names

app.run()
