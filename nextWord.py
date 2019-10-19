# HELLOWORLD 2019
# Program Description:
#
#
#
#
# MODULE IMPORTS
import string
import random

# GLOBALS
filenameList = ["newTest.txt"]
userChoice = 0

# FUNCTION DEFINITIONS
# buildList
def buildList(textFile):
    contents = textFile.read()
    parsedList = []
    wordList = contents.rsplit()
    for word in wordList:
        word = word.translate(str.maketrans('','',string.punctuation))
        word = word.lower()
        parsedList.append(word)
    return parsedList

# make_pairs
def make_pairs(words):
    for i in range(len(words)-1):
        yield (words[i], words[i+1])

# MAIN

print("Training Files: Shakespearean (1)\n")
try:
    userChoice = int(input("Enter your choice of training file: "))
except TypeError:
    print("Invalid input. Program exiting...\n")
    exit(1)

filename = filenameList[userChoice-1]
biglist = []
for f in filenameList:
    try:
        textFile = open(f,"r")
    except FileNotFoundError:
        print('File not found. Program exiting...\n')
        exit(2)
    parsedList = buildList(textFile)
    pairs = make_pairs(parsedList)
    word_dict = {}
    for word_1, word_2 in pairs:
        if word_1 in word_dict.keys():
            word_dict[word_1].append(word_2)
        else:
            word_dict[word_1] = [word_2]
    biglist.append(word_dict)

firstWord = ""
print("Finished Processing\n")
while firstWord != "q":
    firstWord = input("Enter a word: ")
    if firstWord.lower() in word_dict:
        a = biglist[userChoice - 1]
        print(random.choice(a[firstWord.lower()]))
    else:
        print("Not a valid word\n")
