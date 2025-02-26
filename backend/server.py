from flask import Flask
from blockchain import Blockchain

app=Flask(__name__)
bc=Blockchain()

@app.route()
