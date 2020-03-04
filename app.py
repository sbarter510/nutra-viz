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
    try:
        conn = psycopg2.connect(dbname ="nutrition_facts", user="postgres", password="Nikita87")
        cur = conn.cursor()
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        result = cur.execute(f"SELECT name FROM food_facts ;")
        return result
    except(e):
        print(e)
        return e

    #conn.close(
    #return render_template("results.html", results=result)

if __name__ == "__main__":
    app.run(debug=True)
