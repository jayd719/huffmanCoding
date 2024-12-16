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

    def initialize_pq(self, priority_queue: PriorityQueue) -> Node:
        if priority_queue.is_empty():
            raise ValueError("Priority queue is empty")

        while len(priority_queue) > 1:
            # Remove two nodes with the lowest frequency
            left_node = priority_queue.remove()
            right_node = priority_queue.remove()

            # Combine frequencies and create a parent node
            combined_freq = left_node.freq + right_node.freq
            parent_node = Node(None, combined_freq, left_node, right_node)

            # Insert the parent node back into the priority queue
            priority_queue.insert(parent_node)

        # The last remaining node is the root of the Huffman tree
        self.root = priority_queue.remove()
        return self.root

    def _write_node_recursive(self, node: Node, file_handle) -> None:
        if node is not None:
            file_handle.write(f"{node}\n")
            self._write_node_recursive(node.left, file_handle)
            self._write_node_recursive(node.right, file_handle)

    def write_tree_to_file(self, file_path: str = "tree.txt") -> None:
        try:
            with open(file_path, "w", encoding="utf-8") as file_handle:
                self._write_node_recursive(self.root, file_handle)
        except IOError as e:
            raise IOError(f"Error writing to file {file_path}: {e}")

    def initialize_from_freq(self, file_path: str = "frequency.txt") -> Node:
        priority_queue = PriorityQueue()

        try:
            with open(file_path, "r", encoding="utf-8") as file_handle:
                for line in file_handle:
                    char, freq = line.split(":")
                    freq = int(freq)
                    priority_queue.insert(Node(char, freq))
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {file_path}")
        except ValueError:
            raise ValueError(f"Invalid line format in file {file_path}. Expected 'char:freq'.")
        except IOError as e:
            raise IOError(f"Error reading from file {file_path}: {e}")

        return self.initialize_pq(priority_queue)
