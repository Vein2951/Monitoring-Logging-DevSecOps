from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    feature_enabled = os.getenv("NEW_DASHBOARD", "false").lower() == "true"

    if feature_enabled:
        return "<h1>New Dashboard Enabled</h1>"

    return "<h1>Old Dashboard Enabled</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
