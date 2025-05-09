from flask import request,Flask,jsonify
from flask_cors import CORS
from blockchain import Blockchain
from helperfunc import convert_to_json
from model import modelPredect

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "home"

@app.route('/get-user-details/<Id>')
def get_details(Id):
    Id = int(Id)
    user_data = blockchain.get_block(Id)
    print(user_data)
    user_data = convert_to_json(user_data)
    return jsonify(user_data)

@app.route('/insert-data',methods=['POST'])
def insert_data():
    data = request.get_json()
    blockchain.add_medical_record(data)
    block_data = blockchain.mine_block()
    print(block_data)
    return jsonify({"success": True, "block_data": block_data}) 

@app.route('/analysis',methods=['POST'])
def predict():
    info = request.get_json()
    print(info)
    predection = modelPredect(info)
    print(predection)
    return jsonify(predection)
@app.route('/basic')
def displayhome():
    ans = blockchain.get_last_block()
    block = ans['index']
    lasthash = ans['hash']
    Tosend = {
        'Blocks':block,
        'lasthash':lasthash
    }
    return jsonify(Tosend)

if __name__ == "__main__" :
    blockchain = Blockchain()
    app.run(debug=True)