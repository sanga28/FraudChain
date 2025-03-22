from web3 import Web3
import joblib
import pandas as pd

# Connect to Ethereum network
rpc_url = "http://127.0.0.1:8545"  # Local Hardhat node
web3 = Web3(Web3.HTTPProvider(rpc_url))

# Ensure connected
assert web3.is_connected(), "Failed to connect to the Ethereum network"

# Load the fraud model and encoder
model = joblib.load('model/fraud_model.pkl')
encoder = joblib.load('model/label_encoder.pkl')

# Smart contract details
contract_address = "YOUR_CONTRACT_ADDRESS"  # Replace with deployed contract address
contract_abi = [
    {
        "inputs": [
            {"internalType": "uint256", "name": "_id", "type": "uint256"},
            {"internalType": "uint256", "name": "_amount", "type": "uint256"},
            {"internalType": "string", "name": "_location", "type": "string"},
            {"internalType": "bool", "name": "_isFraud", "type": "bool"}
        ],
        "name": "addTransaction",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    }
]

# Load contract
contract = web3.eth.contract(address=contract_address, abi=contract_abi)

# Function to interact with the contract
def send_to_blockchain(txn_id, amount, location):
    location_encoded = encoder.transform([location])[0]

    # Predict fraud status using the AI model
    txn_data = pd.DataFrame([[amount, location_encoded]], columns=['Amount', 'Location'])
    prediction = model.predict(txn_data)[0]
    is_fraud = bool(prediction)

    # Send transaction details to the smart contract
    tx = contract.functions.addTransaction(
        txn_id, int(amount), location, is_fraud
    ).transact({'from': web3.eth.accounts[0]})
    
    receipt = web3.eth.wait_for_transaction_receipt(tx)
    print("Transaction receipt:", receipt)

# Example test
send_to_blockchain(1001, 2000, "California")
