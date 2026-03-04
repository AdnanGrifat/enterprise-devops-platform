from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.get("/")
def root():
    return jsonify(service="enterprise-sample-app", status="ok"), 200

@app.get("/healthz")
def health():
    return jsonify(status="ok"), 200

if __name__ == "__main__":
    port = int(os.getenv("PORT", "5000"))
    app.run(host="0.0.0.0", port=port)
