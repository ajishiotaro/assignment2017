import sys
from nltk.tokenize import sent_tokenize

file_name = sys.argv[1]

openedFile = open(file_name).read()
sent_tokenize_list = sent_tokenize(openedFile)
print(sent_tokenize_list)
