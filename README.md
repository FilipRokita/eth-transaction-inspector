# Ethereum Transaction Inspector

A Python script that connects to the Ethereum network using Infura and retrieves details of a specified transaction.

---

## Features

- Connects to the Ethereum mainnet using the Infura API.
- Retrieves and displays the following transaction details:
  - **To Address**: The recipient of the transaction.
  - **Gas Price**: The gas price paid for the transaction (in wei).
  - **Input Call Data**: The data sent with the transaction, displayed in hexadecimal format.
- Handles errors gracefully, including invalid transaction hashes or connectivity issues.

---

## Prerequisites

1. Python 3.8 or later installed.
2. An Infura account with a registered project. Get your project ID from [Infura](https://infura.io/).
3. Installed Python dependencies:
   - `web3`
   - `python-dotenv`

---

## Installation

1. Clone this repository or download the script file.
2. Install the required Python libraries:
   ```bash
   pip install web3 python-dotenv
