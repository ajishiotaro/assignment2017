import sys
import re

file_name = sys.argv[1]

for line in open(file_name):
    line = line.strip()
    sp = re.split(" +",line)
    for i in range(len(sp)):
        print(sp[i])
