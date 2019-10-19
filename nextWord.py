# HELLOWORLD 2019
# Program Description:
#
#
#
#
# MODULE IMPORTS
import string
import numpy as py

# FUNCTIONS DEFINITIONS
def buildList(textFile):
    contents = textFile.read()
    parsedList = []
    wordList = contents.rsplit(' ')
    for word in wordList:
        word = word.translate(str.maketrans('','',string.punctuation))
        word = word.lower()
        word = word.rstrip()
        parsedList.append(word)
    return parsedList

def make_pairs(words):
    for i in range(len(words)-1):
        yield (words[i], words[i+1])

# MAIN
textFile = open("testData.txt","r")
parsedList = buildList(textFile)
pairs = make_pairs(parsedList)
word_dict = {}
for word_1, word_2 in pairs:
    if word_1 in word_dict.keys():
        word_dict[word_1].append(word_2)
    else:
        word_dict[word_1] = [word_2]

print(word_dict)
