from flask import Flask, jsonify, request
from cipher.playfair import PlayfairCipher

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "PlayFair API is running",
        "status": "ok"
    })


@app.route("/api/playfair/encrypt", methods=["POST"])
def encrypt_playfair():
    try:
        data = request.get_json(force=True)

        key = data.get("key", "")
        plaintext = data.get("plaintext", "")

        cipher = PlayfairCipher(key)
        ciphertext = cipher.encrypt(plaintext)

        return jsonify({
            "success": True,
            "ciphertext": ciphertext,
            "matrix": cipher.matrix_to_text()
        })
    except Exception as error:
        return jsonify({
            "success": False,
            "error": str(error)
        }), 400


@app.route("/api/playfair/decrypt", methods=["POST"])
def decrypt_playfair():
    try:
        data = request.get_json(force=True)

        key = data.get("key", "")
        ciphertext = data.get("ciphertext", "")

        cipher = PlayfairCipher(key)
        plaintext = cipher.decrypt(ciphertext)

        return jsonify({
            "success": True,
            "plaintext": plaintext,
            "matrix": cipher.matrix_to_text()
        })
    except Exception as error:
        return jsonify({
            "success": False,
            "error": str(error)
        }), 400


@app.route("/api/playfair/matrix", methods=["POST"])
def create_matrix():
    try:
        data = request.get_json(force=True)

        key = data.get("key", "")

        cipher = PlayfairCipher(key)

        return jsonify({
            "success": True,
            "matrix": cipher.matrix_to_text()
        })
    except Exception as error:
        return jsonify({
            "success": False,
            "error": str(error)
        }), 400


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
