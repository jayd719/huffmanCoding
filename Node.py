class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.right = None
        self.left = None

    def __lt__(self, otherNode) -> bool:
        return self.freq < otherNode.freq

    def __str__(self) -> str:
        return f"{self.char}:{self.freq}"