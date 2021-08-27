from flask import Flask, jsonify, abort, make_response
import pandas as pd

NOT_FOUND = 'Not found'
BAD_REQUEST = 'Bad request'

app = Flask(__name__)

#Simulating Read From DB
users = pd.read_csv('users.csv')  # read CSV
users = users.to_dict(orient="records")

def _get_user(id):
    return [user for user in users if user['userId'] == id]

def _record_exists(name):
    return [user for user in users if user["name"] == name]

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': NOT_FOUND}), 404)

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': BAD_REQUEST}), 400)

@app.route('/api/v1.0/hello', methods=['GET'])
def get():
    return jsonify({'hello': 'world'})

@app.route('/api/v1.0/users', methods=['GET'])
def get_items():
    return jsonify({'users': users})

@app.route('/api/v1.0/users/<int:id>', methods=['GET'])
def get_item(id):
    user = _get_user(id)
    if not user:
        abort(404)
    return jsonify({'user': user})

if __name__ == '__main__':
    app.run(debug=True)
