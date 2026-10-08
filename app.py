import os
from flask import Flask, jsonify, send_from_directory

app = Flask(__name__)

BASE = os.path.dirname(os.path.abspath(__file__))

# Supabase Project URL
SUPABASE_URL = "https://hgytaserclznpdvsprcj.supabase.co"

# YAHAN apni sb_publishable_... wali PUBLIC key paste karo
SUPABASE_ANON_KEY = "sb_publishable_BelI6AFqTe0fv4oVlazXwg_udFGAPy2"


@app.route("/")
def home():
    return send_from_directory(BASE, "index.html")


@app.route("/config")
def config():
    return jsonify({
        "url": SUPABASE_URL,
        "anonKey": SUPABASE_ANON_KEY
    })


@app.route("/health")
def health():
    return "ok"


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )
