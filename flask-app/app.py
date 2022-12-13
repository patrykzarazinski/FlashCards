from flask import Flask, render_template
import sqlite3

DATABASENAME = "words.db"


class Database:
    def __init__(self):
        try:
            self._connection = sqlite3.connect(DATABASENAME)
            self._cursor = self._connection.cursor()
        except Exception as e:
            print(f"Can not connect to database. Exception occurred: {e}")

    def execute(self, sql, parameters=(), /):
        self._cursor.execute(sql, parameters)
        self._connection.commit()

    def __del__(self):
        self._cursor.close()
        self._connection.close()


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/action')
def action():
    return render_template('action.html')


if __name__ == "__main__":
    db = Database()
    app.run(host="0.0.0.0", port=5000, debug=False)
