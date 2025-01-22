from web3 import Web3


def main():
    """
    Main function to construct input call data for transferring 100 USDC tokens.
    """

    # Address of the recipient
    recipient_address = "0x85b931A32a0725Be14285B66f1a22178c672d69B"

    # Option 2: Ask the user to input the recipient's address
    # Commented out, due to the task requirements.
    # recipient_address = input("Enter the recipient's address: ").strip()
    
    # Amount of USDC to transfer (100 USDC = 100 * 10^6 in the smallest units)
    transfer_amount = 100 * 10**6

    # Option 2: Ask the user to input the amount to transfer
    # Commented out, due to the task requirements.
    # transfer_amount = int(input("Enter the amount of USDC to transfer: ").strip

    # Generate the input call data
    input_data = construct_input_data(recipient_address, transfer_amount)

    # Print the constructed input call data
    print(f"Constructed Input Call Data: {input_data}")


def construct_input_data(to_address, amount):
    """
    Constructs input call data for the ERC-20 transfer function.
    
    Args:
        to_address (str): The recipient's Ethereum address.
        amount (int): The amount of tokens to transfer in the smallest units (e.g., for USDC, 1 USDC = 10^6).
    
    Returns:
        str: Hexadecimal input call data for the transfer function.
    """

    # Hash of the function signature: transfer(address,uint256)
    function_signature = "transfer(address,uint256)"
    method_id = Web3.keccak(text=function_signature)[:4].hex()  # First 4 bytes of the hash

    # Encode the recipient's address (32 bytes, padded with zeros)
    padded_to_address = to_address[2:].zfill(64)

    # Encode the amount to transfer (32 bytes, padded with zeros)
    padded_amount = hex(amount)[2:].zfill(64)

    # Concatenate all parts to construct the input call data
    return f"0x{method_id}{padded_to_address}{padded_amount}"


if __name__ == "__main__":
    main()
