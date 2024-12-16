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
from PriorityQueue import PriorityQueue


class HuffmanTree:
    def __init__(self):
        self.root = None

    def initialize_pq(self, priority_queue) -> Node:
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

    def write_node_aux(self, node, fh) -> None:
        if node is not None:
            fh.write(f"{node}\n")
            self.write_node_aux(node.left, fh)
            self.write_node_aux(node.right, fh)
        return None

    def write_tree_to_file(self, file_path="tree.txt") -> None:
        fh = open(file_path, "w", encoding="utf-8")
        self.write_node_aux(self.root, fh)
        fh.close()
        return 1

    def intitiale_from_freq(self, file_path="frequency.txt"):
        fh = open(file_path, "r", encoding="utf-8")
        pq = PriorityQueue()
        try:
            line = fh.readline()
            while line is not None and len(line):
                char, freq = (line.strip()).split(":")
                pq.insert(Node(char, int(freq)))
                line = fh.readline()
            fh.close()

            
        except FileNotFoundError:
            raise FileNotFoundError(f"file not found: {file_path}")
        except IOError:
            raise IOError(f"Error Opening File {file_path}")
        
        return self.initialize_pq(pq)

