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
    for word in contents:
        #word = word.translate(str.maketrans("","",string.punctuation))
        #parsedList.append(word)
        print(word)


    for element in parsedList:
      print(element)



# MAIN
textFile = open("test.txt","r")
buildList(textFile)
































