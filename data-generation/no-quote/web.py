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
    res = cur.execute(f"SELECT users FROM users WHERE favorite_number={number}")
    users = res.fetchall()
    users = ','.join(users)
    return users

app.run()
