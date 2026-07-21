from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/date")
def date():
    now = datetime.now()
    status = "EVEN" if now.second % 2 == 0 else "ODD"
    return f"{now.strftime('%H:%M:%S')} {status}"

app.run(host="0.0.0.0", port=2026)

