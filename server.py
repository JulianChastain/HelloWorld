import tornado.escape
import tornado.ioloop
import tornado.web
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
    
print("Finished Processing\n")

def nextWord(userChoice, firstWord):
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

class nextWordHandler(tornado.web.RequestHandler):
    def get(self):
        lastWord = self.get_query_argument("lastWord")
        dialect = self.get_query_argument("dialect")
        suggestions = nextWord(int(dialect), lastWord)
        self.set_header("Content-type", "application/json")
        self.write(tornado.escape.json_encode(suggestions))

def make_app():
        return tornado.web.Application([
            (r"/nextword", nextWordHandler),
            (r"/(.*)", tornado.web.StaticFileHandler, {"path": "Static", "default_filename": "index.html"}),
        ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
