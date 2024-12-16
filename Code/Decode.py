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
from HuffmanTree import HuffmanTree


def DECODE(compressed_file="compressed.bin", freq_table="frequency.txt"):
    ht = HuffmanTree()
    node = ht.initialize_from_freq(freq_table)
    ht.write_tree_to_file("treex.txt")
    # file handler
    fh = open(compressed_file, "rb")
    fh_out = open("decoded.txt", "w", encoding="utf-8")

    encoded_data = fh.read()
    encoded_data = "".join(f"{byte:08b}" for byte in encoded_data)

    for bit in encoded_data:
        if bit == BIT_ZERO:
            node = node.left
        else:
            node = node.right

        if node is None:
            raise ValueError("Invalid bit stream: Reached a non-existent node.")
        
        if node.char:
            fh_out.write(f"{node.char}")
            node = ht.root

    fh.close()
    fh_out.close()


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    logging.info("Starting Huffman Decoding...")
    try:
        DECODE()
    except FileNotFoundError:
        logging.error("The specified file was not found.")
    except ValueError as ve:
        logging.error(f"Value Error: {ve}")
    except Exception as e:
        logging.error("An unexpected error occurred: %s", e)
