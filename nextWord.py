
# will take the previous word entered by the
# Need to analyze the words given in the textfile (testData.txt) and decide the
# probability of what the next word will be
def nextWord(lastword):
  return lastword + "Clemson"

import numpy as py

words = ["hello", "world", "test", "data", "hello", "us"]

def make_pairs(words):
    for i in range(len(words)-1):
        yield (words[i], words[i+1])

pairs = make_pairs(words)

word_dict = {}

for word_1, word_2 in pairs:
    if word_1 in word_dict.keys():
        word_dict[word_1].append(word_2)
    else:
        word_dict[word_1] = [word_2]

print(word_dict)
