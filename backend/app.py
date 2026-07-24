"""
NovaStart intake backend
-------------------------
A minimal, production-sane Flask API that receives the contact/intake
form as JSON, validates it, and stores it (here: an in-memory list +
append-only JSON-lines file — swap for a real database when ready).

Run locally:
    pip install -r requirements.txt
    python app.py
Server starts on http://127.0.0.1:5000
"""

import os
import re
import json
from datetime import datetime, timezone

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

# --- CORS --------------------------------------------------------
# Allows your frontend (running on a different domain/port) to call
# this API. In production, restrict this to your actual frontend
# domain instead of "*" — see the comment below.
ALLOWED_ORIGINS = [
    "http://127.0.0.1:5500",
    "http://localhost:5500",
    "http://localhost:3000",
    "https://startup-portfolio-one.vercel.app",
]

CORS(
    app,
    origins=ALLOWED_ORIGINS,
    methods=["GET", "POST", "OPTIONS"],
    allow_headers=["Content-Type"],
)

EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
SUBMISSIONS_FILE = os.path.join(os.path.dirname(__file__), "submissions.jsonl")


def validate_payload(data: dict):
    """Returns a list of field-level error strings; empty list = valid."""
    errors = []
    name = (data.get("name") or "").strip()
    email = (data.get("email") or "").strip()
    message = (data.get("message") or "").strip()

    if not name:
        errors.append("Name is required.")
    if not email or not EMAIL_RE.match(email):
        errors.append("A valid email is required.")
    if not message or len(message) < 10:
        errors.append("Please describe your project in at least 10 characters.")

    return errors


@app.route("/api/health", methods=["GET"])
def health():
    """Simple uptime check — useful for Render/Railway health checks."""
    return jsonify({"status": "ok"}), 200


@app.route("/api/contact", methods=["POST"])
def contact():
    if not request.is_json:
        return jsonify({"error": "Request body must be JSON."}), 400

    data = request.get_json(silent=True) or {}
    errors = validate_payload(data)

    if errors:
        return jsonify({"error": " ".join(errors)}), 400

    record = {
        "name": data.get("name", "").strip(),
        "email": data.get("email", "").strip(),
        "company": (data.get("company") or "").strip(),
        "budget": (data.get("budget") or "").strip(),
        "message": data.get("message", "").strip(),
        "received_at": datetime.now(timezone.utc).isoformat(),
    }

    # Persist as append-only JSON-lines. Good enough for an MVP;
    # replace with a real DB (Postgres, SQLite, etc.) before scaling.
    try:
        with open(SUBMISSIONS_FILE, "a", encoding="utf-8") as f:
            f.write(json.dumps(record) + "\n")
    except OSError as e:
        app.logger.error("Failed to write submission: %s", e)
        return jsonify({"error": "Server storage error. Please try again shortly."}), 500

    app.logger.info("New intake from %s <%s>", record["name"], record["email"])
    return jsonify({"message": "Intake received.", "data": record}), 201

@app.route("/api/submissions", methods=["GET"])
def submissions():
    try:
        with open(SUBMISSIONS_FILE, "r", encoding="utf-8") as f:
            data = [json.loads(line) for line in f]
        return jsonify(data), 200
    except FileNotFoundError:
        return jsonify([]), 200

if __name__ == "__main__":
    # Render/Railway inject PORT; default to 5000 for local dev.
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)