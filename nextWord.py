# HELLOWORLD 2019
# Program Description:
#
#
#
#






















# MODULE IMPORTS
import string


# FUNCTIONS DEFINITIONS

def buildList(textFile):
    contents = textFile.read()
    parsedList = []
    wordList = contents.rsplit(' ')
    for word in wordList:
        word = word.translate(str.maketrans('','',string.punctuation))
        word = word.lower()
        word = word.rstrip('\n')
        parsedList.append(word)
    return parsedList


# MAIN
textFile = open("test.txt","r")
parsedList = buildList(textFile)












<<<<<<< HEAD
=======
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
>>>>>>> fc10dafc1cef20f1bb04ffbb023b1ef5ce391451
