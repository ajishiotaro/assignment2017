import sys
from nltk.tokenize import sent_tokenize, word_tokenize

file_name = sys.argv[1]

openedFile = open(file_name).read()
sent_tokenize_list = sent_tokenize(openedFile)
word_tokenize_list = []

for sent in sent_tokenize_list:
    words = word_tokenize(sent)
    word_tokenize_list.append(words)
    
print(word_tokenize_list)
