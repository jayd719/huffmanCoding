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


def build_frequency_table(file_handler) -> dict:
    # Builds a frequency table from file content (lowercased).
    frequency_table = Counter(file_handler.read().lower())
    return dict(frequency_table)


def build_priority_queue(freqeuncy_table) -> PriorityQueue:
    # Creates a priority queue from a frequency table.
    pq = PriorityQueue()
    for char, freq in freqeuncy_table.items():
        pq.insert(Node(char, freq))
    return pq


def build_huffman_tree(priority_queue) -> Node:
    # Builds a Huffman tree from a priority queue.
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
    # Recursively generates encoding map from a Huffman tree.
    if node.char:
        encoding_map[node.char] = encoded_text
    else:
        depth_first_search(node.left, encoded_text + "0", encoding_map)
        depth_first_search(node.right, encoded_text + "1", encoding_map)


def build_encoding_map(root) -> dict:
    # Creates an encoding map from the Huffman tree root.
    encoding_map = {}
    depth_first_search(root, "", encoding_map)
    return encoding_map


def encode(fh, encoding_map) -> str:
    # Encodes file content into a binary string using an encoding map.
    return "".join(encoding_map[char] for char in fh.read().lower())


def decode(encoded_text, root):
    # Decodes a binary string using the Huffman tree.
    decoded_text = ""
    node = root
    for bit in encoded_text:
        if bit == "0":
            node = node.left
        else:
            node = node.right

        if node.char:
            decoded_text += node.char
            node = root
    return decoded_text


if __name__ == "__main__":
    fh = open("input.txt", "r", encoding="utf-8")
    f = build_frequency_table(fh)
    fh.close()
    pq = build_priority_queue(f)
    tree_root_node = build_huffman_tree(pq)
    encoding_map = build_encoding_map(tree_root_node)
    fh = open("input.txt", "r", encoding="utf-8")
    encoded_text = encode(fh, encoding_map)
    fh.close()
    print(encoded_text)
    decoded_text = decode(encoded_text, tree_root_node)
    print(decoded_text)
