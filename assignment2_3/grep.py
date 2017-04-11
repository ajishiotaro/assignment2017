ximport sys
import re

file_name = sys.argv[1]
grep_word = sys.argv[2]
r = re.compile(grep_word)

for line in open(file_name):
    if (r.search(line)):
        print(line, end = "")
