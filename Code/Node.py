"""
-------------------------------------------------------
Assignment 5 Node
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      169018282
Email:   sing8282@mylaurier.ca
__updated__ = "2024-12-5"
-------------------------------------------------------
"""


class Node:
    # Represents a node
    def __init__(self, char, freq, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other) -> bool:
        if self.freq == other.freq:
            return self.char < other.char if self.char and other.char else False
        return self.freq < other.freq

    def __str__(self) -> str:
        # Returns a string representation of the node.
        return f"{self.char}:{self.freq}"
