from flask import Flask, request, jsonify
import joblib
from web3 import Web3
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()

# Ethereum Setup
infura_url = os.getenv('INFURA_URL')
web3 = Web3(Web3.HTTPProvider(infura_url))
contract_address = "YOUR_CONTRACT_ADDRESS"
private_key = "YOUR_PRIVATE_KEY"

# Load Model
model = joblib.load('model/fraud_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    prediction = model.predict([data['features']])[0]

    # Store prediction on blockchain
    tx = web3.eth.contract(address=contract_address, abi=contract_abi).functions.storeTransaction(
        data['sender'], data['receiver'], data['amount'], bool(prediction)
    ).transact({'from': web3.eth.accounts[0]})
    
    return jsonify({'fraud': bool(prediction), 'transaction': tx.hex()})

if __name__ == '__main__':
    app.run(debug=True)
