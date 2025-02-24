from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit
from blockchain import Blockchain

app = Flask(__name__)
socketio = SocketIO(app)
bc = Blockchain()

@app.route('/add_validator', methods=['POST'])
def add_validator():
    data = request.json
    bc.add_validator(data['validator_id'], data['role'])
    return jsonify({"message": "Validator added"}), 200

@app.route('/add_block', methods=['POST'])
def add_block():
    data = request.json
    try:
        block = bc.add_block(data['data'], data['validator'])
        return jsonify({"message": "Block added", "block": block.__dict__}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 403

@app.route('/get_records/<patient_id>', methods=['GET'])
def get_records(patient_id):
    records = bc.get_patient_records(patient_id)
    return jsonify(records), 200

@app.route('/register_node', methods=['POST'])
def register_node():
    node_address = request.json['node_address']
    bc.register_node(node_address)
    return jsonify({"message": "Node registered"}), 200

@socketio.on('connect')
def handle_connect():
    print("New node connected")

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
