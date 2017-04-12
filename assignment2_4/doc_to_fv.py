import sys
import shelve
from collections import OrderedDict
from nltk.tokenize import sent_tokenize, word_tokenize

file_name = sys.argv[1]

openedFile = open(file_name).read()
sent_tokenize_list = sent_tokenize(openedFile)
word_tokenize_list = []

for sent in sent_tokenize_list:
    words = word_tokenize(sent)
    word_tokenize_list.extend(words)

count = OrderedDict()
index = shelve.open("freq_to_index_shelve.db")
try:
    countOfIndex = len(index) + 1 
    for i in word_tokenize_list:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
            if not i in index:
                index[i] = countOfIndex
                countOfIndex += 1

    feature_vector = [0] * len(index)

    for k,v in count.items():
        feature_vector[index[k] - 1] = v

    for j in range(len(feature_vector)):
        if feature_vector[j] != 0:
            print(str(j + 1) + ":" + str(feature_vector[j]), end = " ")
    print()

finally:
    index.close()
        
    
