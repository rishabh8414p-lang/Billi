import os
from flask import Flask, jsonify, send_from_directory

app = Flask(__name__)
BASE = os.path.dirname(os.path.abspath(__file__))


@app.route("/")
def home():
    return send_from_directory(BASE, "index.html")


@app.route("/config")
def config():
    # Sirf PUBLIC anon key. service_role key kabhi yahan mat daalna.
    return jsonify(
        url=os.environ.get("SUPABASE_URL", ""),
        anonKey=os.environ.get("SUPABASE_ANON_KEY", ""),
    )


@app.route("/health")
def health():
    return "ok"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
