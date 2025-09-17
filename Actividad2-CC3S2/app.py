import os
from flask import Flask, jsonify, request

PORT = int(os.environ.get("PORT", "8080"))
MESSAGE = os.environ.get("MESSAGE", "Hola CC3S2")
RELEASE = os.environ.get("RELEASE", "v1")

app = Flask(__name__)

@app.route("/", methods=["GET"])
def root():
    app.logger.info("GET / from %s", request.remote_addr)
    return jsonify({
        "message": MESSAGE,
        "release": RELEASE,
        "client": request.remote_addr
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
