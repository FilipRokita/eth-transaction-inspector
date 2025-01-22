# ETH Transaction Inspector

A Python script that connects to the Ethereum network using Infura and retrieves details of a specified transaction.

## Features

- Connects to the Ethereum mainnet using the Infura API.
- Retrieves and displays the following transaction details:
    - **To Address**: The recipient of the transaction.
    - **Gas Price**: The gas price paid for the transaction (in wei).
    - **Input Call Data**: The data sent with the transaction, displayed in hexadecimal format.
- Handles errors gracefully, including invalid transaction hashes or connectivity issues.

## Prerequisites

1. Python 3.12 or later installed.
2. An Infura (MetaMask Developer) account with a registered project.
3. Installed required Python dependencies.

## Installation

1. Clone this repository.
2. Install the required Python libraries:
    ```bash
    pip install -r requirements.txt
    ```
3. Create a `.env` file in the script directory and add your Infura URL:
    ```
    INFURA_URL=https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID
    ```