from pprint import pprint
from typing import Counter


sentence = "This is a com mon interview question"
set_characters = {*sentence}
print(set_characters)
dict_characters = {}


for char in set_characters:
    value = 0
    for letter in sentence:
        if char == letter:
            value += 1
    dict_characters[char] = value


def get_max_value(dict):
    max_value = 0
    key_max_value = ""
    for k, v in dict.items():
        if v >= max_value:
            key_max_value = k
            max_value = v
    return (key_max_value, max_value)


print(get_max_value(dict_characters))
print(dict_characters)

# Mosh solution

char_frequency = {}
for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

char_frequency_sorted = sorted(
    char_frequency.items(),
    key=lambda kv: kv[1],
    reverse=True)

pprint(char_frequency_sorted, width=20)
print(char_frequency_sorted[0])
