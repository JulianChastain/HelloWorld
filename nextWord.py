
# will take the previous word entered by the
# Need to analyze the words given in the textfile (testData.txt) and decide the
# probability of what the next word will be
def nextWord(lastword):
  return lastword + "Clemson"

#from https://github.com/ashwinmj/word-prediction/blob/master/MarkovModel.ipynb
import string
import numpy as np

# Path of the text file containing the training data
training_data_file = 'testData.txt'

#Helper functions
def remove_punctuation(sentence):
    return sentence.translate(str.maketrans('','', string.punctuation))


def add2dict(dictionary, key, value):
    if key not in dictionary:
        dictionary[key] = []
    dictionary[key].append(value)


def list2probabilitydict(given_list):
    probability_dict = {}
    given_list_length = len(given_list)
    for item in given_list:
        probability_dict[item] = probability_dict.get(item, 0) + 1
    for key, value in probability_dict.items():
        probability_dict[key] = value / given_list_length
    return

initial_word = {}
second_word = {}
transitions = {}

# Trains a Markov model based on the data in training_data_file
def train_markov_model():
    for line in open(training_data_file):
        tokens = remove_punctuation(line.rstrip().lower()).split()
        tokens_length = len(tokens)
        for i in range(tokens_length):
            token = tokens[i]
            if i == 0:
                initial_word[token] = initial_word.get(token, 0) + 1
            else:
                prev_token = tokens[i - 1]
                if i == tokens_length - 1:
                    add2dict(transitions, (prev_token, token), 'END')
                if i == 1:
                    add2dict(second_word, prev_token, token)
                else:
                    prev_prev_token = tokens[i - 2]
                    add2dict(transitions, (prev_prev_token, prev_token), token)

    # Normalize the distributions
    initial_word_total = sum(initial_word.values())
    for key, value in initial_word.items():
        initial_word[key] = value / initial_word_total

    for prev_word, next_word_list in second_word.items():
        second_word[prev_word] = list2probabilitydict(next_word_list)

    for word_pair, next_word_list in transitions.items():
        transitions[word_pair] = list2probabilitydict(next_word_list)

    print('Training successful.')

def sample_word(dictionary):
    p0 = np.random.random()
    cumulative = 0
    for key, value in dictionary.items():
        cumulative += value
        if p0 < cumulative:
            return key
    assert(False)


firstWord = input()
print(sample_word(second_word[firstWord]))
