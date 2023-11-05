# Project Name: EduTOz

## Problem:
Developers interested in building on the Tezos blockchain often face challenges due to limited educational resources. The existing materials are insufficient to provide a solid foundation for development.

## Solution:
EduTOz is an educative platform designed to address this issue by offering a comprehensive learning experience and incentivizing community participation.

## Product Details:

#### 1) Learning Module:

- Description: This module provides a series of basic exercises aimed at helping users build proficiency in Tezos development.
- Reward System: Upon completing an exercise, participants earn tokens. These tokens serve as a form of recognition and are non-transferable.

#### 2) Project Collaboration Space:

- Description: Companies can submit projects to the platform, inviting the community to develop solutions.
- Voting System: 
	- The community evaluates the proposed projects through a voting mechanism. The weightage is distributed with companies holding 40% and the community holding 60%.
	- The weight of each vote is determined by the voter's rank, which is determined by his or her token balance. You will find all the details in this file : VotingCalculusMethod.md.
- Reward System:
	- Voting for the best projects earns you tokens.
	- Voting for less popular projects may result in a loss of tokens, potentially impacting the voter's rank position.
	- Error Detection Algorithm: Voters who have supported a project with detected errors lose tokens.
- Winner Selection: The project with the highest combined score wins. The company sets a prize at the outset, and the winning project automatically wins this prize.

#### 3) Developer Hiring Service:

- Description: Our company maintains a dataset of users, including their proficiency in various fields of development.
- Functionality: Companies seeking developers with specific skills can utilize our service to access relevant information and potentially hire developers from the community.

## Benefits:

- Provides a structured learning path for Tezos development.
- Fosters collaboration between companies and the Tezos community.
- Incentivizes active participation with a token-based reward system.
- Enables expert developers to earn money while continuing to learn through new projects.
- Offers visibility into the market's evolution, showcasing which companies are actively contributing.
- It offers a learning opportunity for beginners and intermediates, allowing them to carry out the project and then correct themselves thanks to the winning project.

## MVP Achieved:

#### 1) Website Creation:

- Description: A dedicated website is created to serve as the user interface for EduTOz.
- Functionality:
	- Provides an intuitive and user-friendly interface for participants to access the learning module, submit projects, and vote.
	- Displays project details, exercise progress, and leaderboard information.
	- Allows companies to create projects, view submissions, and engage with the community.
   
#### 2) Smart Contracts:

##### - Escrow Smart Contract:
- Functionality: Allows companies to create a project and provide the price.
- Process:
	- Company deposits funds into the escrow contract.
	- Company creates a project.

##### - Vote Smart Contract:
- Functionality: Manages the entire voting system.
- Process:
	- Community members have voted for the projects. They vote with their tokens within a certain limit, depending on their rank. They are partially refunded according to their vote.
	- Once the winner is determined, the vote smart contract automatically sends the public key of the winner to the escrow contract.
	- Escrow releases the funds to the winning project.

##### -Token Smart Contract:
- Functionality: Handles the distribution of tokens as rewards for completing exercises and participating in the platform.
- Process:
	- Tokens are awarded to participants upon completing exercises.
	- Tokens may also be distributed as rewards for active participation in the platform.

## Installation

### Package managers
Here we will use yarn and not npm.

#### 1) With yarn:
a) Install yarn via npm: npm install --global yarn
b) Create a new Vite project: yarn create vite my-project
cd my-project
d) Install dependencies: yarn
c) Run the project: yarn run dev

#### 1) Bis) With npm:
a) Install Node.js and npm here: https://nodejs.org/
b) Create a new Vite project: npx create-vite@latest my-project
cd my-project
c) Run the project: npm run dev

#### QuickStart:
- If you git clone the repo and you have the node_modules
- You need to delete the node_modules file
- And do a npm i

