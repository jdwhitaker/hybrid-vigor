import sqlite3
from flask import Flask, request
import logging

logging.basicConfig(filename='malicious.log',level=logging.DEBUG)

app = Flask(__name__)

@app.route("/query/<name>")
def query(name):
    app.logger.debug(request.path)
    con = sqlite3.connect("web.db")
    cur = con.cursor()
    res = cur.execute(f"SELECT favorite_number FROM users WHERE name='{name}'")
    favorite_number = res.fetchone()[0]
    return str(favorite_number)

app.run()
