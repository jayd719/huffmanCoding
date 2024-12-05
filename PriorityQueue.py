import heapq
from Node import Node


class PriorityQueue:
    def __init__(self):
        self.heap = []

    def __str__(self) -> str:
        return " ".join(str(node) for node in self.heap)

    def is_empty(self) -> bool:
        return len(self.heap) == 0

    def insert(self, node) -> None:
        heapq.heappush(self.heap, node)

    def remove(self) -> Node:
        assert self.is_empty(), "Cannot Remove From Empty Queue"
        return heapq.heappop(self.heap)

