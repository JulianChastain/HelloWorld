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
filenameList = ["shakespeare.txt", "beyonce.txt", "bible.txt"]
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


biglist = []
for f in filenameList:
    try:
        textFile = open(f,"r", encoding="utf8")
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

'''print("Training Files: Shakespearean (1)\n Beyonce (2)\n Biblical(3)")
try:
    userChoice = int(input("Enter your choice of training file: "))
except TypeError:
    print("Invalid input. Program exiting...\n")
    exit(1)'''


print("Finished Processing\n")

def returnWord(userChoice, firstWord):
    if firstWord.lower() in word_dict:
        a = biglist[userChoice]
        nextwordlist = a[firstWord.lower()]
        finalList = []
        attempts = 0
        while len(finalList) < 3 and attempts < 20:
            word = random.choice(nextwordlist)
            if word not in finalList:
                finalList.append(word)
            attempts += 1
        return finalList
    else:
        return []

print(returnWord(0, "thou"))
