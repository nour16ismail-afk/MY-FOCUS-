from flask import Flask, send_from_directory
import os

app = Flask(**name**)

@app.route("/")
def home():
return send_from_directory(".", "index.html")

@app.route("/style.css")
def style():
return send_from_directory(".", "style.css")

if **name** == "**main**":
port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port, debug=False)
