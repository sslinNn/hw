import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [amount, setAmount] = useState(0);
  const [currency, setCurrency] = useState('USD');

  const createTransaction = async () => {
    try {
      const response = await axios.post('http://localhost:5000/transactions', {
        amount,
        currency,
      });
      console.log('Transaction created', response.data);
    } catch (error) {
      console.error('Error creating transaction', error);
    }
  };

  return (
    <div>
      <h2>Create Transaction</h2>
      <input
        type="number"
        value={amount}
        onChange={(e) => setAmount(e.target.value)}
        placeholder="Amount"
      />
      <input
        type="text"
        value={currency}
        onChange={(e) => setCurrency(e.target.value)}
        placeholder="Currency"
      />
      <button onClick={createTransaction}>Create Transaction</button>
    </div>
  );
}

export default App;