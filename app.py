from flask import Flask, render_template, Response, jsonify
import pandas as pd
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/data/<input>")
def results(input):
    input = input.capitalize()
    try:
        conn = psycopg2.connect(dbname ="nutrition_facts", user="postgres", password="Nikita87")
        cur = conn.cursor()
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur.execute(f"SELECT name FROM food_facts \
                    WHERE NAME LIKE '{input}%'; ")
    except(e):
        return(e)
    return render_template("results.html", results=cur.fetchall())

if __name__ == "__main__":
    app.run(debug=True)
