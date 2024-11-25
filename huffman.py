import heapq
from collections import defaultdict

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def huffman_encoding(data):
    if not data:
        return "", {}

    # Calculate frequency of each character
    frequency = defaultdict(int)
    for char in data:
        frequency[char] += 1

    # Create a priority queue (min-heap)
    heap = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)

    # Build the Huffman Tree
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    # Generate codes
    root = heap[0]
    huffman_codes = {}
    _generate_codes(root, "", huffman_codes)

    # Encode the data
    encoded_data = ''.join(huffman_codes[char] for char in data)
    return encoded_data, huffman_codes

def _generate_codes(node, current_code, huffman_codes):
    if node is None:
        return
    if node.char is not None:
        huffman_codes[node.char] = current_code
    _generate_codes(node.left, current_code + "0", huffman_codes)
    _generate_codes(node.right, current_code + "1", huffman_codes)

def huffman_decoding(encoded_data, huffman_codes):
    reversed_codes = {v: k for k, v in huffman_codes.items()}
    current_code = ""
    decoded_output = ""

    for bit in encoded_data:
        current_code += bit
        if current_code in reversed_codes:
            decoded_output += reversed_codes[current_code]
            current_code = ""

    return decoded_output
