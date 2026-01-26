from flask import Flask, jsonify, request, render_template
import json
import os

app = Flask(__name__)

# -----------------------------
# Load rules from JSON at startup
# -----------------------------
def load_rules():
    with open("data/rules.json", "r") as file:
        return json.load(file)

rules_data = load_rules()

# -----------------------------
# Required input fields
# -----------------------------
REQUIRED_FIELDS = [
    "public_wifi",
    "password_protected",
    "shared_network",
    "router_age"
]

# -----------------------------
# Rule matching logic
# -----------------------------
def rule_matches(user_input, rule_conditions):
    for key, value in rule_conditions.items():
        if user_input.get(key) != value:
            return False
    return True

# -----------------------------
# Routes
# -----------------------------

# Home page (UI)
@app.route("/")
def home():
    return render_template("index.html")

# Health check endpoint
@app.route("/health")
def health():
    return jsonify({
        "status": "ok",
        "rules_loaded": len(rules_data["rules"])
    })

# Risk assessment API
@app.route("/assess", methods=["POST"])
def assess():
    # 1️⃣ Read form data
    user_input = {
        "public_wifi": request.form.get("public_wifi"),
        "password_protected": request.form.get("password_protected"),
        "shared_network": request.form.get("shared_network"),
        "router_age": request.form.get("router_age")
    }

    # 2️⃣ Validate required fields
    missing_fields = [
        field for field in REQUIRED_FIELDS
        if not user_input.get(field)
    ]

    if missing_fields:
        return jsonify({
            "error": "Missing required fields",
            "missing_fields": missing_fields
        }), 400

    # 3️⃣ Rule evaluation
    for rule in rules_data["rules"]:
        if rule_matches(user_input, rule["conditions"]):
            return render_template(
                "result.html",
                risk_level=rule["risk_level"],
                explanation=rule["explanation"],
                recommendation=rule["recommendation"]
            )

    # 4️⃣ No rule matched
    return render_template(
        "result.html",
        risk_level="Unknown",
        explanation="Inputs were provided, but no matching rule was found.",
        recommendation="Please review your answers or update the rule set."
    )

# -----------------------------
# Run the application
# -----------------------------
if __name__ == "__main__":
    debug_mode = os.getenv("FLASK_DEBUG", "false").lower() == "true"
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=5000, debug=debug_mode)