from flask import Flask, render_template, jsonify, request
import time
import json
import datetime

app = Flask(__name__, static_url_path='/static')

class data:
    interactions = []
    flag_saved=False
    def __init__(self,reload=True):
        if reload:
            data.flag_saved=False
            data.interactions=[]
        return

    def append_data(self,in_data):
        data.interactions.append(in_data)
        return

    def file_name(self):
        current_datetime = datetime.datetime.now()
        timestamp = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")
        return f"data_{timestamp}.txt"

    def save_data(self):
        if data.flag_saved is False:
            with open(self.file_name(), "w") as textile_file:
                textile_file.write(str(data.interactions))
            data.flag_saved=True
        return

CONSTANT_DATA=data()

@app.route("/")
def index():
    CONSTANT_DATA=data(True)
    return render_template("index.html")

@app.route("/record_interaction", methods=["POST"])
def record_interaction():
    data = request.json
    CONSTANT_DATA.append_data(data)
    return jsonify({"status": "OK"})

@app.route("/save_interaction", methods=["POST"])
def save_interaction():
    with open("output.txt", "w") as textile_file:
        CONSTANT_DATA.save_data()
    return jsonify({"status": "OK"})

if __name__ == "__main__":
    app.run(debug=True)
