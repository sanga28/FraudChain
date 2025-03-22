import { useState } from "react";
import axios from "axios";
import "../styles/Form.css";

const TransactionForm = () => {
  const [amount, setAmount] = useState("");
  const [location, setLocation] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);

    try {
      const res = await axios.post(
        `${process.env.REACT_APP_BACKEND_URL}/transactions`,
        { amount, location }
      );
      console.log(res.data);
      alert("Transaction sent!");
    } catch (error) {
      console.error(error);
      alert("Error sending transaction");
    }

    setLoading(false);
  };

  return (
    <div className="form-container">
      <form onSubmit={handleSubmit}>
        <input
          type="number"
          placeholder="Amount"
          value={amount}
          onChange={(e) => setAmount(e.target.value)}
        />
        <input
          type="text"
          placeholder="Location"
          value={location}
          onChange={(e) => setLocation(e.target.value)}
        />
        <button type="submit" disabled={loading}>
          {loading ? "Sending..." : "Send Transaction"}
        </button>
      </form>
    </div>
  );
};

export default TransactionForm;
