import pickle, string
fn = "shakespearepickle"
outfile = open(fn, "wb")

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

# make_pairs
def make_pairs(words):
    return parsedList
    for i in range(len(words)-1):
        yield (words[i], words[i+1])

pairs = make_pairs(parsedList)
word_dict = {}

parsedList = buildList("newTest.txt")
for word_1, word_2 in pairs:
    if word_1 in word_dict.keys():
        word_dict[word_1].append(word_2)
    else:
        word_dict[word_1] = [word_2]

pickle.dump(word_dict, outfile)
outfile.close
print("finished")
