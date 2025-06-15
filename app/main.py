from flask import Flask, render_template
from app.tracker import get_wallet_data  # this pulls your wallet logic

app = Flask(__name__)

@app.route("/")
def dashboard():
    wallet_data = get_wallet_data()
    print("DEBUG:", wallet_data)  # Add this line
    return render_template("dashboard.html", data=wallet_data)