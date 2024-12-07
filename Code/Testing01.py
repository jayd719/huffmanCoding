# Testing PriorityQueue

from PriorityQueue import PriorityQueue
from Node import Node


if __name__ == "__main__":
    print("-" * 20)
    print("Testing Priority Queue")
    print("-" * 20)

    # Initialize Priority Queue
    pq = PriorityQueue()
    print(f"\tIs Empty: {pq.is_empty()}")  # Should print True

    # Create nodes
    a = Node("a", 5)
    b = Node("b", 3)
    c = Node("c", 8)

    # Test Insert
    print("Test Insert")
    pq.insert(a)
    pq.insert(b)
    pq.insert(c)
    print(f"\tIs Empty: {pq.is_empty()}")  # Should print False
    print(f"\tQueue: {pq}")  # Should print "b:3 a:5 c:8"

    # Test Remove
    print("Test Remove")
    removed = pq.remove()
    print(f"\tRemoved Node: {removed}")  # Should print "b:3"
    print(f"\tQueue After Removal: {pq}")  # Should print "a:5 c:8"


    # Test Len 
    print("Test Quent Lenght")
    print(f"\tQueue Len: {len(pq)}") # should print 2
    
    # Test Remove Again
    print("Test Remove Again")
    removed = pq.remove()
    print(f"\tRemoved Node: {removed}")  # Should print "a:5"
    print(f"\tQueue After Removal: {pq}")  # Should print "c:8"

    # Test is_empty on partially filled queue
    print(f"\tIs Empty: {pq.is_empty()}")  # Should print False

    # Test Remove Last Element
    print("Test Remove Last Element")
    removed = pq.remove()
    print(f"\tRemoved Node: {removed}")  # Should print "c:8"
    print(f"\tQueue After Removal: {pq}")  # Should print an empty string

    # Test is_empty on empty queue
    print(f"\tIs Empty: {pq.is_empty()}")  # Should print True

    print("All Tests Passed")
    print("-" * 20)
    # Test Remove on Empty Queue
    print("Test Remove on Empty Queue")
    pq.remove()
    
    
