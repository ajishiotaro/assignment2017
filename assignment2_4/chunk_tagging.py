import sys
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tag import SennaTagger, SennaChunkTagger

file_name = sys.argv[1]

openedFile = open(file_name).read()
sent_tokenize_list = sent_tokenize(openedFile)
word_tokenize_list = []

for sent in sent_tokenize_list:
    words = word_tokenize(sent)
    word_tokenize_list.append(words)
    
tagger = SennaChunkTagger("/usr/share/senna-v3.0")

tags = tagger.tag(word_tokenize_list[0])

flag = True

for pair in tags:
    if pair[1][0] == "B" or pair[1][0] == "O":
        if not flag:
            print()
        else:
            flag = False
        if pair[1][0] == "B":
            print(pair[1][2:], end = " ")
        else:
            print(pair[1], end = " " )
    print(pair[0], end = " ")
    
print()    
