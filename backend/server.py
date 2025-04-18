from flask import request,Flask,jsonify
from blockchain import Blockchain
from helperfunc import convert_to_json

app = Flask(__name__)

@app.route('/')
def home():
    return "home"

@app.route('/get-user-details/<Id>')
def get_details(Id):
    Id = int(Id)
    user_data = blockchain.get_block(Id)
    user_data = convert_to_json(user_data)
    return jsonify(user_data)


if __name__ == "__main__" :
    blockchain = Blockchain()
    app.run(debug=True)