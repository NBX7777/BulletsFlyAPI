from flask import Flask, request, jsonify

app = Flask(__name__)

# 關鍵字 -> 對應多張圖片
meme_map = {
    "噁心": ["https://imgur.com/a/rA0M9y0"],
    "翻譯翻譯": ["https://imgur.com/a/vREicB4"],
    "公平": ["https://imgur.com/h4af9O4"],
}


@app.route("/meme", methods=["POST"])
def get_meme():
    if request.is_json:
        data = request.get_json()
        text = data.get("text", "")

        result_images = []

        for keyword, img_list in meme_map.items():
            if keyword in text:
                result_images.extend(img_list)  # 把這個關鍵字對應的圖片都加進結果

        if result_images:
            return jsonify({"image_urls": result_images})
        else:
            return jsonify({"image_urls": ["https://imgur.com/aeFk9vN"]})

    else:
        return jsonify({"error": "Request must be JSON"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
