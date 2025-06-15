from flask import Flask, render_template
from app.tracker import get_wallet_data  # this pulls your wallet logic

import os
app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), 'templates'))



@app.route("/")
def dashboard():
    wallet_data = get_wallet_data()
    print("DEBUG:", wallet_data)  # Add this line
    return render_template("dashboard.html", data=wallet_data)