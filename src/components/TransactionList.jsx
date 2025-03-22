import { useEffect, useState } from "react";
import axios from "axios";
import "../styles/Transactions.css";

const TransactionList = () => {
  const [transactions, setTransactions] = useState([]);

  useEffect(() => {
    const fetchTransactions = async () => {
      const res = await axios.get(
        `${process.env.REACT_APP_BACKEND_URL}/transactions`
      );
      setTransactions(res.data);
    };

    fetchTransactions();
  }, []);

  return (
    <div className="transaction-list">
      <h2>Transactions</h2>
      {transactions.map((tx, index) => (
        <div key={index} className="transaction-item">
          <p><strong>Location:</strong> {tx.location}</p>
          <p><strong>Amount:</strong> {tx.amount} ETH</p>
          <p><strong>Status:</strong> {tx.isFraud ? "Fraudulent" : "Safe"}</p>
        </div>
      ))}
    </div>
  );
};

export default TransactionList;
