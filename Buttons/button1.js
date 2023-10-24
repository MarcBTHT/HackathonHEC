import { TezosToolkit } from '@taquito/taquito';

const Tezos = new TezosToolkit('https://mainnet.smartpy.io'); // Remplacez par l'URL du nœud Tezos que vous utilisez
Tezos.setProvider({
  wallet: 'temple-wallet',
});


async function stopVote() {
    const contractAddressVote = 'KT1CPT4rXYzsaL3HTzzwdjr7hXjA5Rag3zcS'; 
    const contractVote = await Tezos.wallet.at(contractAddressVote);
  
    let resultVoteFn = await contractVote.methods.result_voting().send();


    const contractAddressEscrow = 'KT1RJJM28zJqT3DX61C4iD3oweEdg8FghBFw';
    const contractEscrow = await Tezos.wallet.at(contractAddressEscrow);
    await contractEscrow.methods.reward(resultVoteFn).send();

    //await contract.methods.reset_voting().send();

    await operation.confirmation();
    console.log('Transaction confirmed :', operation);
  }




  
<button onClick={stopVote}>Stop the vote and send the cash prize to the winner</button>

