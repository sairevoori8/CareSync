import hashlib
import datetime
import json
from dbConnection import get_db, get_cipher  # Import encryption functions

class Blockchain:
    def __init__(self):
        self.db = get_db()
        self.collection = self.db["medicalrecords"]
        self.cipher = get_cipher()  # Get the cipher for encryption

        self.chain = []
        self.pending_records = []

        if self.collection.count_documents({}) == 0:
            self.create_genesis_block()
        else:
            self.load_chain_from_db()

    def create_genesis_block(self):
        genesis_block = {
            'index': 1,
            'timestamp': str(datetime.datetime.now()),
            'records': [],
            'previous_hash': "0",
            'nonce': 0,
            'hash': self.calculate_hash(1, [], "0", 0)
        }
        self.chain.append(genesis_block)
        self.collection.insert_one(genesis_block)

    def encrypt_data(self, data):
        """Encrypts medical data."""
        json_data = json.dumps(data)  # Convert to JSON string
        encrypted = self.cipher.encrypt(json_data.encode())  # Encrypt
        return encrypted.decode()  # Convert bytes to string

    def decrypt_data(self, encrypted_data):
        """Decrypts medical data."""
        decrypted = self.cipher.decrypt(encrypted_data.encode()).decode()  # Decrypt and convert to string
        return json.loads(decrypted)  # Convert JSON string back to dictionary

    def calculate_hash(self, index, records, previous_hash, nonce):
        block_string = json.dumps({
            'index': index,
            'records': records,
            'previous_hash': previous_hash,
            'nonce': nonce
        }, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()

    def proof_of_work(self, index, records, previous_hash):
        nonce = 0
        while True:
            hash_value = self.calculate_hash(index, records, previous_hash, nonce)
            if hash_value[:4] == "0000":  # Proof-of-work difficulty
                return nonce, hash_value
            nonce += 1

    def add_medical_record(self,record_dict):
        """Encrypts and adds medical records."""
        encrypted_record = self.encrypt_data(record_dict)  # Encrypt the entire record
        self.pending_records.append(encrypted_record)
        return f"Encrypted record added to pending transactions (Total: {len(self.pending_records)})"

    def mine_block(self):
        if not self.pending_records:
            return "No pending records to mine."

        previous_block = self.chain[-1]
        index = previous_block['index'] + 1
        previous_hash = previous_block['hash']
        nonce, block_hash = self.proof_of_work(index, self.pending_records, previous_hash)

        new_block = {
            'index': index,
            'timestamp': str(datetime.datetime.now()),
            'records': self.pending_records,  # Encrypted records
            'previous_hash': previous_hash,
            'nonce': nonce,
            'hash': block_hash
        }

        self.chain.append(new_block)
        self.collection.insert_one(new_block)
        self.pending_records = []

        re_dict={
            'index':index,
            'hash':block_hash
        }
        return re_dict

    def load_chain_from_db(self):
        self.chain = list(self.collection.find().sort("index", 1))

    def get_last_block(self):
        return self.chain[-1] if self.chain else None

    def get_block(self, index):
        """Retrieves and decrypts a block's records by index."""
        block = self.collection.find_one({"index": index})
        if not block:
            return "Block not found."

        decrypted_records = [self.decrypt_data(record) for record in block["records"]]
        block["records"] = decrypted_records  # Replace encrypted records with decrypted ones
        return block
