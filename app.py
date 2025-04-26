from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return "Welcome to BulletsFlyAPI!"


@app.route("/meme", methods=["POST"])
def get_meme():
    if request.is_json:
        data = request.get_json()
        text = data.get("text", "")

        return jsonify(
            {"text_received": text, "meme_url": "https://imgur.com/b6wGgOg.jpg"}
        )
    else:
        return jsonify({"error": "Request must be JSON"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
