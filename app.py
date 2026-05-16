from flask import Flask, render_template, request, jsonify
from config import Config
import random
import string
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',
                           bot_name=Config.BOT_NAME,
                           telegram=Config.TELEGRAM_OWNER,
                           bg_img=Config.ANIME_IMG)

@app.route('/generate-code', methods=['POST'])
def generate_code():
    phone = request.json.get('number')
    if not phone:
        return jsonify({"success": False})

    code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4)) + "-" + \
           ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))

    return jsonify({"success": True, "code": code})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)