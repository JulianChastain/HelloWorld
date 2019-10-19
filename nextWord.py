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
filenameList = ["shakespeare.txt"]
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
try:
    userChoice = int(input("Enter your choice of training file: "))
except TypeError:
    print("Invalid input. Program exiting...")
    exit(1)

filename = filenameList[userChoice-1]

try:
    textFile = open("newTest.txt","r")
except FileNotFoundError:
    print('File not found. Program exiting...')
    exit(2)

parsedList = buildList(textFile)
pairs = make_pairs(parsedList)
word_dict = {}
for word_1, word_2 in pairs:
    if word_1 in word_dict.keys():
        word_dict[word_1].append(word_2)
    else:
        word_dict[word_1] = [word_2]

firstWord = ""
print("Finished Processing")
while firstWord != "done":
    firstWord = input()
    if firstWord.lower() in word_dict:
        print(random.choice(word_dict[firstWord.lower()]))
    else:
        print("Not a valid word")
    print("\n")
