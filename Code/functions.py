"""
-------------------------------------------------------
Assignment 5 Custom Functions Library
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      169018282
Email:   sing8282@mylaurier.ca
__updated__ = "2024-12-5"
-------------------------------------------------------
"""

# IMPORTS
from PriorityQueue import PriorityQueue
from collections import Counter
from Node import Node
import argparse
import logging
import re
import os
from utilis import *


# CONSTANTS
BIT_ZERO = "0"
BIT_ONE = "1"


# FUNCTIONS
def build_frequency_table(file_path) -> dict:
    """
    Builds a frequency table by streaming through the file line by line.
    """
    try:
        frequency_table = Counter()
        with open(file_path, "r", encoding="utf-8") as file_handler:
            for line in file_handler:
                processed_line = re.sub(r"\s+", " ", line.lower())
                if not processed_line.strip():
                    continue
                frequency_table.update(processed_line)
                logging.debug(f"Text_Encoded: {line}")

    except FileNotFoundError:
        raise FileNotFoundError(f"File '{file_path}' not found.")
    except IOError:
        raise IOError(f"Error Opening file {file_path}")

    return dict(frequency_table)


def build_priority_queue(frequency_table) -> PriorityQueue:
    """
    Creates a priority queue from a frequency table.
    """
    pq = PriorityQueue()
    for char, freq in frequency_table.items():
        pq.insert(Node(char, freq))
    return pq


def build_huffman_tree(priority_queue) -> Node:
    """
    Builds a Huffman tree from a priority queue.
    """
    if priority_queue.is_empty():
        raise ValueError("Priority queue is empty")

    while len(priority_queue) > 1:
        node_a = priority_queue.remove()
        node_b = priority_queue.remove()
        parent_freq = node_a.freq + node_b.freq
        parentNode = Node(None, parent_freq, node_a, node_b)
        priority_queue.insert(parentNode)
    return priority_queue.remove()


def depth_first_search(node, encoded_text, encoding_map) -> None:
    """
    Recursively generates encoding map from a Huffman tree.
    """
    if node.char:
        encoding_map[node.char] = encoded_text
    else:
        depth_first_search(node.left, encoded_text + BIT_ZERO, encoding_map)
        depth_first_search(node.right, encoded_text + BIT_ONE, encoding_map)


def build_encoding_map(root) -> dict:
    """
    Creates an encoding map from the Huffman tree root.
    """
    encoding_map = {}
    depth_first_search(root, "", encoding_map)
    return encoding_map


def encode(file_path, encoding_map) -> str:
    """
    Encodes file content into a binary string using an encoding map by streaming the file.
    """
    encoded_text = []
    try:
        with open(file_path, "r", encoding="utf-8") as file_handler:
            for line in file_handler:
                for char in re.sub(r"\s+", " ", line.lower()):
                    encoded_text.append(encoding_map[char])
    except FileNotFoundError:
        raise FileNotFoundError(f"file not found: {file_path}")
    except IOError:
        raise IOError(f"Error Opening File {file_path}")
    return "".join(encoded_text)


def decode(encoded_text, root) -> str:
    """
    Decodes a binary string using the Huffman tree.
    """
    decoded_text = []
    node = root
    for bit in encoded_text:
        if bit == BIT_ZERO:
            node = node.left
        else:
            node = node.right

        if node.char:
            decoded_text.append(node.char)
            node = root
    return "".join(decoded_text)


def encoding_stats(file_path, output_file) -> None:
    original_size = os.path.getsize(file_path)
    encoded_size = os.path.getsize(output_file)
    compression_ratio = round((encoded_size / original_size) * 100, 2)
    # log info
    logging.info(f"ORGINAL SIZE: {original_size} Bytes")
    logging.info(f"Compressed Size: {encoded_size} Bytes")
    logging.info(f"Compression Ratio: {compression_ratio} %")
    return None


def DECODE(encoded_text, tree_root_node):
    decoded_text = decode(encoded_text, tree_root_node)
    return decoded_text


# decoded_text = DECODE(encoded_text, root)
# logging.debug(f"Decoded Text: {decoded_text}")
