"""
-------------------------------------------------------
Assignment 5 Decode
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      169018282
Email:   sing8282@mylaurier.ca
__updated__ = "2024-12-5"
-------------------------------------------------------
"""

from functions import *



def DECODE(encoded_text, tree_root_node):
    decoded_text = decode(encoded_text, tree_root_node)
    return decoded_text






if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logging.info("Starting Huffman Decoding...")
    try:
        Input_file = "compressed.bin"
    except FileNotFoundError:
        logging.error("The specified file was not found.")
    except ValueError as ve:
        logging.error(f"Value Error: {ve}")
    except Exception as e:
        logging.error("An unexpected error occurred: %s", e)
