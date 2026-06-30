from flask import Flask, render_template, request
import sqlite3
import pandas as pd

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():

    conn = sqlite3.connect("products.db")

    if request.method == "POST":

        keyword = request.form["search"]

        query = f"""
        SELECT *
        FROM products
        WHERE Title LIKE '%{keyword}%'
        """

        df = pd.read_sql_query(query, conn)

    else:

        df = pd.read_sql_query("SELECT * FROM products", conn)

    conn.close()

    products = df.to_dict(orient="records")

    return render_template("index.html", products=products)

if __name__ == "__main__":
    app.run(debug=True)