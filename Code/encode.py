"""
-------------------------------------------------------
Assignment 5 Encode
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      169018282
Email:   sing8282@mylaurier.ca
__updated__ = "2024-12-5"
-------------------------------------------------------
"""

from functions import *
from HuffmanTree import HuffmanTree


def ENCODE(file_path, output_file):
    """
    Performs the entire encoding process.
    """
    frequency_table = build_frequency_table(file_path)
    if not frequency_table:
        return ""
    
    write_table_to_disk(frequency_table)
    priority_queue = build_priority_queue(frequency_table)
    
    ht = HuffmanTree()
    ht.initialize_pq(priority_queue)
    ht.write_tree_to_file()
    
    encoding_map = build_encoding_map(ht.root)
    write_table_to_disk(encoding_map, "codes.txt")
    
    encoded_text = encode(file_path, encoding_map)
    write_encoded_text(encoded_text)
    
    encoding_stats(file_path, output_file)
    return encoded_text


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    parser = argparse.ArgumentParser(description="Huffman Encoding/Decoding")
    parser.add_argument("file_path", help="Path to the input text file")
    args = parser.parse_args()
    logging.info("Starting Huffman Encoding")
    try:
        output_file = "compressed.bin"
        encoded_text = ENCODE(args.file_path, output_file)
    except FileNotFoundError:
        logging.error("The specified file was not found.")
    except ValueError as ve:
        logging.error(f"Value Error: {ve}")
    except Exception as e:
        logging.error("An unexpected error occurred: %s", e)
