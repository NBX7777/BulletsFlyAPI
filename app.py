from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/meme", methods=["POST"])
def get_meme():
    data = request.get_json()
    text = data.get("text")

    # 假設固定回傳一張梗圖網址
    return jsonify({"text_received": text, "meme_url": "https://imgur.com/b6wGgOg.jpg"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
