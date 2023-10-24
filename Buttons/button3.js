import React, { useState } from 'react';
import { TezosToolkit } from '@taquito/taquito';

const ContractVote = () => {
  const [inputString, setInputString] = useState('');
  
  const handleInputChange = (event) => {
    setInputString(event.target.value);
  };

  const handleInteraction = async () => {
    const contractAddress = 'KT1CPT4rXYzsaL3HTzzwdjr7hXjA5Rag3zcS'; // Remplacez par l'adresse de votre contrat
    const contract = await Tezos.wallet.at(contractAddress);

    try {
      const operation = await contract.methods.vote_for_candidate(inputString).send();
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
        placeholder="Insert team name"
        value={inputString}
        onChange={handleInputChange}
      />
      <button onClick={handleInteraction}>Interagir avec le contrat</button>
    </div>
  );
};

export default ContractVote;