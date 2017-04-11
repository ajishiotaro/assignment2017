import sys
from collections import OrderedDict
from nltk.tokenize import sent_tokenize, word_tokenize

file_name = sys.argv[1]

openedFile = open(file_name).read()
sent_tokenize_list = sent_tokenize(openedFile)
word_tokenize_list = []

for sent in sent_tokenize_list:
    words = word_tokenize(sent)
    word_tokenize_list.append(words)
    
count = OrderedDict()
for i in word_tokenize_list:
    for j in i:
        if j in count:
            count[j] += 1
        else:
            count[j] = 1

for k,v in sorted(count.items(), key = lambda x:x[1]):
    print(v,k)
