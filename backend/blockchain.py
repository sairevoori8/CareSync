import hashlib
import time
import json
from uuid import uuid4
from cryptography.fernet import Fernet

class Block:
    def __init__(self, index, previous_hash, timestamp, data, validator):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.validator = validator
        self.hash = self.calculate_hash()
    
    def calculate_hash(self):
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.validators = set()
        self.roles = {}
        self.encryption_key = Fernet.generate_key()
        self.cipher = Fernet(self.encryption_key)
        self.nodes = set()
    
    def create_genesis_block(self):
        return Block(0, "0", time.time(), "Genesis Block", "System")
    
    def add_validator(self, validator_id, role):
        self.validators.add(validator_id)
        self.roles[validator_id] = role
    
    def encrypt_data(self, data):
        return self.cipher.encrypt(json.dumps(data).encode()).decode()
    
    def decrypt_data(self, encrypted_data):
        return json.loads(self.cipher.decrypt(encrypted_data.encode()).decode())
    
    def add_block(self, data, validator):
        if validator not in self.validators:
            raise ValueError("Unauthorized validator")
        if self.roles.get(validator) not in ["doctor", "admin"]:
            raise ValueError("Insufficient permissions")
        
        encrypted_data = self.encrypt_data(data)
        last_block = self.chain[-1]
        new_block = Block(len(self.chain), last_block.hash, time.time(), encrypted_data, validator)
        self.chain.append(new_block)
        return new_block
    
    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            prev, curr = self.chain[i - 1], self.chain[i]
            if curr.previous_hash != prev.hash or curr.hash != curr.calculate_hash():
                return False
        return True
    
    def get_patient_records(self, patient_id):
        records = []
        for block in self.chain:
            try:
                decrypted_data = self.decrypt_data(block.data)
                if decrypted_data.get("patient_id") == patient_id:
                    records.append(decrypted_data)
            except:
                continue
        return records
    
    def register_node(self, node_address):
        self.nodes.add(node_address)
