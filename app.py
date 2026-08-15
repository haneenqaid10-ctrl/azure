import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World 🦋"

if name == "main":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
