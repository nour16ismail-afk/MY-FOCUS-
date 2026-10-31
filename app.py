from flask import Flask, send_from_directory
import os

BASE_DIR = os.path.dirname(os.path.abspath(**file**))

app = Flask(**name**)

@app.route("/")
def home():
return send_from_directory(BASE_DIR, "index.html")

@app.route("/style.css")
def style():
return send_from_directory(BASE_DIR, "style.css")

@app.route("/healthz")
def health():
return "OK", 200

if **name** == "**main**":
port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port, debug=False)
