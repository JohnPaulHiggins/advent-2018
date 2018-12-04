#!/usr/bin/python

def string_letter_count(s):
    counts_dictionary = dict()
    for letter in set(s):
        counts_dictionary[letter] = s.count(letter)
    return counts_dictionary


with open('./input.txt') as f:
    counts = list(map(string_letter_count, f))

two_count = len([word for word in counts if (2 in word.values())])
three_count = len([word for word in counts if (3 in word.values())])

print(two_count * three_count)
