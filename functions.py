from collections import Counter
from Node import Node
from PriorityQueue import PriorityQueue


def build_frequency_table(file_handler):
    frequency_table = Counter(file_handler.read().lower())
    return dict(frequency_table)


def build_priority_queue(freqeuncy_table):
    pq = PriorityQueue()
    for char, freq in freqeuncy_table.items():
        pq.insert(Node(char, freq))
    return pq


def build_huffman_tree(priority_queue):

    node_a = priority_queue.remove()
    node_b = priority_queue.remove()

    return


fh = open("input.txt", "r", encoding="utf-8")
f = build_frequency_table(fh)
pq = build_priority_queue(f)
print(len(pq))
build_huffman_tree(pq)
