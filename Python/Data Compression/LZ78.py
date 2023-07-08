'''
Written by nuggetbucket54

========== COMPRESSION LOGIC ==========

1. Start with an empty dictionary and an empty input buffer.
2. Read symbols from the input data one at a time.
3. Initialize a prefix as an empty string.
4. Append the current symbol to the prefix.
5. If the prefix is already in the dictionary, update the prefix by
   appending the current symbol and repeat step 5.
6. If the prefix is not in the dictionary, add the prefix to the dictionary with a unique index
   and output the index of the previous prefix and the current symbol.
7. Clear the prefix and repeat from step 4 until all symbols are processed.

========== DECOMPRESSION LOGIC ==========

During decompression, the algorithm uses the dictionary entries to reconstruct the original data.
It reads the index and symbol pairs, retrieves the corresponding phrases from the dictionary, and
outputs them to reconstruct the original data.
'''

def compress(data):
    storage = {"": 0}
    compressed_data = []
    current_symbol = ""
    index = 1
    for character in data:
        current_symbol += character
        if current_symbol not in storage:
            storage[current_symbol] = index
            compressed_data.append((storage[current_symbol[:-1]], character))
            index += 1
            current_symbol = ""
    return compressed_data

print(compress("ABBCBCABABCAABCAAB"))

