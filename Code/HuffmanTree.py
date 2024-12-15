"""
-------------------------------------------------------
Assignment 5 Huffman Tree
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      169018282
Email:   sing8282@mylaurier.ca
__updated__ = "2024-12-5"
-------------------------------------------------------
"""

from Node import Node


class HuffmanTree:
    def __init__(self):
        self.root = None

    def initialize_pq(self, priority_queue):
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
        self.root = priority_queue.remove()
        return self.root

    def intitiale_preq(file_path):
        return None
