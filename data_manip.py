# Using this to convert to files into a dictionary.

import json

left_file = "wordlist-left.txt"
right_file = "wordlist-right.txt"
output_file = "wordlist.json"

wordlist_keys = []
wordlist_values = []

with open(left_file, "r") as f:
    for line in f:
        wordlist_keys.append(line.strip())

with open(right_file, "r") as f:
    for line in f:
        wordlist_values.append(line.strip())

output_dict = dict(zip(wordlist_keys, wordlist_values))

serialized_dict = json.dumps(output_dict)

with open(output_file, "w") as f:
    f.write(serialized_dict)