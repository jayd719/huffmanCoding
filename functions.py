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

from collections import Counter
from Node import Node
from PriorityQueue import PriorityQueue
import re


def build_frequency_table(file_path) -> dict:
    """
    Builds a frequency table by streaming through the file line by line.
    """
    frequency_table = Counter()
    input_text = []
    with open(file_path, "r", encoding="utf-8") as file_handler:
        for line in file_handler:
            processed_line = re.sub(r"\s+", " ", line.lower())
            frequency_table.update(processed_line)
            input_text.append(processed_line)
    return dict(frequency_table), "".join(input_text)


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
        depth_first_search(node.left, encoded_text + "0", encoding_map)
        depth_first_search(node.right, encoded_text + "1", encoding_map)


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
    with open(file_path, "r", encoding="utf-8") as file_handler:
        for line in file_handler:
            for char in re.sub(r"\s+", " ", line.lower()):
                encoded_text.append(encoding_map[char])
    return "".join(encoded_text)


def decode(encoded_text, root) -> str:
    """
    Decodes a binary string using the Huffman tree.
    """
    decoded_text = []
    node = root
    for bit in encoded_text:
        if bit == "0":
            node = node.left
        else:
            node = node.right

        if node.char:
            decoded_text.append(node.char)
            node = root
    return "".join(decoded_text)


if __name__ == "__main__":
    file_path = "input.txt"
    frequency_table, input_text = build_frequency_table(file_path)
    print(f'Text-Encoded: {input_text}')
    priority_queue = build_priority_queue(frequency_table)
    tree_root_node = build_huffman_tree(priority_queue)
    encoding_map = build_encoding_map(tree_root_node)
    encoded_text = encode(file_path, encoding_map)
    print(f"Encoded Text: {encoded_text}")
    decoded_text = decode(encoded_text, tree_root_node)
    print(f"Decoded Text: {decoded_text}")
