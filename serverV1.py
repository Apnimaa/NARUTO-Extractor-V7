import getserver

def connect_server():
    try:
        getserver.connect_v1()
    except Exception as e:
        print("ERROR:", e)

if __name__ == "__main__":
    connect_server()

from flask import Flask
import threading
import os

# Flask app
flask_app = Flask(__name__)

@flask_app.route("/")
def home():
    return "😊 Lovely bot is live"

# Flask run in background
def run():
    flask_app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        debug=False
    )

# Start flask in background thread
threading.Thread(target=run).start()



