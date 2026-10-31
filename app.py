from flask import Flask, render_template
from flask import send_from_directory
import os

app = Flask(**name**, template_folder=".")

@app.route("/")
def home():
return render_template("index.html")

@app.route("/style.css")
def style():
return send_from_directory(".", "style.css")

if **name** == "**main**":
port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port, debug=False)
