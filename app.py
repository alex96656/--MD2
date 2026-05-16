from flask import Flask, render_template, request, jsonify
from config import Config
import random
import string

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', bot_name=Config.BOT_NAME, telegram=Config.TELEGRAM_OWNER, bg_img=Config.ANIME_IMG)

@app.route('/generate-code', methods=['POST'])
def generate_code():
    phone = request.json.get('number')
    if not phone: return jsonify({"success": False})
    
    # Random pairing code generation
    code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4)) + "-" + \
           ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    
    return jsonify({"success": True, "code": code})

if __name__ == '__main__':
    app.run(host=Config.WEB_HOST, port=Config.WEB_PORT)
