# Description: A Python script to inspect the details of a transaction on the Ethereum network.
# Author: Filip Rokita


# Import required libraries
import os
from web3 import Web3
from dotenv import load_dotenv


def main():
    """
    Main function to inspect the details of a transaction on the Ethereum network.
    """

    # Load environment variables from .env file
    load_dotenv()
    INFURA_URL = os.getenv("INFURA_URL")
    
    # Check if INFURA_URL is set
    if not INFURA_URL:
        print("INFURA_URL is missing. Please add it to your .env file.")
        return

    # Initialize a Web3 instance
    web3 = Web3(Web3.HTTPProvider(INFURA_URL))

    # Check connection to Ethereum network
    if not web3.is_connected():
        print("Failed to connect to the Ethereum network. Check your INFURA_URL.")
        return

    # Transaction hash to inspect
    transaction_hash = "0x2ad2bb00718ab0ed8310dacff9c029ea5d41e038d96c9f52561a1e7948759e99"
    
    # Option 2: Ask the user to input the transaction hash
    # Commented out, due to the task requirements.
    # transaction_hash = input("Enter the transaction hash: ").strip()

    # Fetch and print the transaction details
    try:
        # Fetch transaction details
        transaction = web3.eth.get_transaction(transaction_hash)

        # Print the required details
        print(f"To Address: {transaction['to']}")
        print(f"Gas Price: {transaction['gasPrice']} wei")
        print(f"Input Call Data: {transaction['input'].hex()}")
    
    # Handle exceptions
    except Exception as e:
        print(f"An error occurred while fetching the transaction details: {e}")


# Run the main function
if __name__ == "__main__":
    main()
