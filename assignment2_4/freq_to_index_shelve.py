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
    countOfIndex = 1
    for i in word_tokenize_list:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
            index[i] = countOfIndex
            countOfIndex += 1
finally:
    index.close()
            
index = shelve.open("freq_to_index_shelve.db")
try:
    for k,v in sorted(index.items(), key = lambda x:x[1]):
        print(v,k)

finally:
    index.close()
        
    
