import React, { useState } from 'react';
import { TezosToolkit } from '@taquito/taquito';

const ContractCreateCandidate = () => {
  const [inputString1, setInputString1] = useState('');
  const [inputString2, setInputString2] = useState('');
  
  const handleInputChange1 = (event) => {
    setInputString1(event.target.value);
  };

  const handleInputChange2 = (event) => {
    setInputString2(event.target.value);
  };

  const handleInteraction = async () => {
    const contractAddress = 'KT1CPT4rXYzsaL3HTzzwdjr7hXjA5Rag3zcS'; 
    const contract = await Tezos.wallet.at(contractAddress);

    try {
      const operation = await contract.methods.add_candidate(value=inputString1, candidate=inputString2).send();
      await operation.confirmation();
      console.log('Transaction confirmed :', operation);
    } catch (error) {
      console.error('Transaction error :', error);
    }
  };

  return (
    <div>
      <input
        type="text"
        placeholder="Insert team address"
        value={inputString1}
        onChange={handleInputChange1}
      />
      <input
        type="text"
        placeholder="Insert team name"
        value={inputString2}
        onChange={handleInputChange2}
      />
      <button onClick={handleInteraction}>Create Candidate</button>
    </div>
  );
};

export default ContractCreateCandidate;