from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/paint", methods=["POST"])
def paint():
    data = request.json
    # TODO: Save the paint data to a database or file
    return jsonify({"status": "OK"})

if __name__ == "__main__":
    app.run(debug=True)
