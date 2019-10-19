# HELLOWORLD 2019
# Program Description:
#
#
#
#
# MODULE IMPORTS
import string
import numpy as py
import random

# FUNCTIONS DEFINITIONS
def buildList(textFile):
    contents = textFile.read()
    parsedList = []
    wordList = contents.rsplit()
    for word in wordList:
        word = word.translate(str.maketrans('','',string.punctuation))
        word = word.lower()
        #word = word.replace('\n','')
        parsedList.append(word)
    return parsedList

def make_pairs(words):
    for i in range(len(words)-1):
        yield (words[i], words[i+1])

# MAIN
textFile = open("newTest.txt","r")
parsedList = buildList(textFile)
pairs = make_pairs(parsedList)
word_dict = {}
for word_1, word_2 in pairs:
    if word_1 in word_dict.keys():
        word_dict[word_1].append(word_2)
    else:
        word_dict[word_1] = [word_2]

while True:
    firstWord = input()
    if firstWord.lower() in word_dict:
        print(random.choice(word_dict[firstWord]))
    else:
        print("Not a valid word")
    print("\n")
