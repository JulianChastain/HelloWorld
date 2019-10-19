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

































