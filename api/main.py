from flask import Flask, request
from db import init_db, get_user, add_user

app = Flask(__name__)

@app.route('/user/<id>', methods=["GET"])
def get_user_by_id(id):
    return get_user(id)

@app.route('/user', methods=["POST"])
def addu():
    data = request.json
    add_user(data)
    return 'succ'

if __name__ == '__main__':
    init_db()
    app.run(debug=True, host='0.0.0.0')