"""
-------------------------------------------------------
Assignment 5 Priority Queue
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      169018282
Email:   sing8282@mylaurier.ca
__updated__ = "2024-12-5"
-------------------------------------------------------
"""

import heapq
from Node import Node


class PriorityQueue:
    # Implements a priority queue using a min-heap.
    def __init__(self):
        # Initializes an empty priority queue.
        self.heap = []

    def __str__(self) -> str:
        # Returns a string representation of the queue.
        return " ".join(str(node) for node in self.heap)

    def __len__(self):
        # Returns the number of elements in the queue.
        return len(self.heap)

    def is_empty(self) -> bool:
        # Checks if the queue is empty
        return len(self.heap) == 0

    def insert(self, node) -> None:
        # Adds a node to the queue.
        heapq.heappush(self.heap, node)

    def remove(self) -> Node:
        # Removes and returns the node with the smallest value.
        assert not self.is_empty(), "Cannot Remove From Empty Queue"
        return heapq.heappop(self.heap)
