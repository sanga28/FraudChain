// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract FraudDetection {
    struct Transaction {
        uint256 id;
        uint256 amount;
        string location;
        bool isFraud;
    }

    mapping(uint256 => Transaction) public transactions;
    uint256 public transactionCount;

    event TransactionAdded(uint256 id, uint256 amount, string location, bool isFraud);

    // Add a new transaction with fraud status
    function addTransaction(
        uint256 _id,
        uint256 _amount,
        string memory _location,
        bool _isFraud
    ) public {
        transactions[_id] = Transaction(_id, _amount, _location, _isFraud);
        transactionCount++;

        emit TransactionAdded(_id, _amount, _location, _isFraud);
    }

    // Get transaction details by ID
    function getTransaction(uint256 _id)
        public
        view
        returns (uint256, uint256, string memory, bool)
    {
        Transaction memory txn = transactions[_id];
        return (txn.id, txn.amount, txn.location, txn.isFraud);
    }
}
