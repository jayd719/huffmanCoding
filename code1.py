from collections import Counter

class Node():
    def __init__(self,char,freq):
        self.char = char
        self.freq = freq
        self.right = None
        self.left = None
        pass


def build_frequency_table(file_handler):
    frequency_table = Counter(file_handler.read().lower())
    return dict(frequency_table)


fh = open("input.txt", "r", encoding="utf-8")
f = build_frequency_table(fh)
print(f)

