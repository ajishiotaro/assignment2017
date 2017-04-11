import sys
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tag import SennaTagger

file_name = sys.argv[1]

openedFile = open(file_name).read()
sent_tokenize_list = sent_tokenize(openedFile)
word_tokenize_list = []

for sent in sent_tokenize_list:
    words = word_tokenize(sent)
    word_tokenize_list.append(words)
    
tagger = SennaTagger("/usr/share/senna-v3.0")

tags = tagger.tag(word_tokenize_list[0])

for tag in tags:
    print(" ".join(tag))
    
