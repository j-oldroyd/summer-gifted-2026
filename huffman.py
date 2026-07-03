# Implement Huffman coding
import networkx as nx

STRING = "This is super"

# Get frequency list
string = STRING.upper()
frequencies = {}

for letter in string:
    if letter not in frequencies:
        frequencies[letter] = string.count(letter)

code = {}
queue = sorted(frequencies.items(), key=lambda x: x[1])  # put rarest items at front

# Get two letters with smallest frequencies
while len(queue) >= 2:
    (letter1, freq1) = queue[0]
    (letter2, freq2) = queue[1]
    code[letter1+letter2] = [letter1, letter2]
    queue = queue[2:]
    queue.append((letter1+letter2, freq1+freq2))
    queue = sorted(queue, key=lambda x: x[-1])
