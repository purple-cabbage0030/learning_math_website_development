from flask import Flask, render_template, jsonify, request
from flask_jwt_extended import *
from dao import *
from dto import *

app = Flask(__name__)

app.config.update(
    DEBUG = True,
    JWT_SECRET_KEY = "############"
)

jwt = JWTManager(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login_proc():
    user_id = request.form.get("user_id")
    user_pw = request.form.get("user_pw")

    if user_id == member_id and user_pw == member_pw:
        return jsonify(
            result = "200",
            access_token = create_access_token(identity = user_id)
        )

    else:
        return "존재하지 않는 사용자입니다."


if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1", port="5000")