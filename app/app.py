from flask import Flask, jsonify
import os
import sys
import time

app = Flask(__name__)

APP_VERSION = os.getenv("APP_VERSION", "unknown")
GIT_COMMIT = os.getenv("GIT_COMMIT", "unknown")
ENVIRONMENT = os.getenv("ENVIRONMENT", "dev")
FAIL_MODE = os.getenv("FAIL_MODE", "false").lower()


FEATURE_FLAG = "ENABLED"

@app.route("/feature")
def feature():
    return jsonify(
        feature="new-endpoint",
        status=FEATURE_FLAG,
        commit=GIT_COMMIT
    )



@app.route("/health")
def health():
    if FAIL_MODE == "true":
        return jsonify(status="unhealthy"), 500
    return jsonify(status="ok"), 200


@app.route("/version")
def version():
    return jsonify(
        version=APP_VERSION,
        commit=GIT_COMMIT,
        environment=ENVIRONMENT
    ), 200


@app.route("/status")
def status():
    return jsonify(
        uptime="running",
        environment=ENVIRONMENT
    ), 200



if __name__ == "__main__":
    print("Starting backend service...")
    print(f"Version: {APP_VERSION}")
    print(f"Commit: {GIT_COMMIT}")
    print(f"Environment: {ENVIRONMENT}")

    # Simulate crash if needed (for later rollback tests)
    if FAIL_MODE == "crash":
        print("FAIL_MODE=crash → exiting")
        sys.exit(1)

    app.run(host="0.0.0.0", port=8080)
