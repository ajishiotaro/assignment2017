import sys
import re
import difflib
from collections import OrderedDict

file_name = sys.argv[1]
#comp_file = sys.argv[2]

count = OrderedDict()
for line in open(file_name):
    line = line.strip()
    sp = re.split(" +",line)
    for i in range(len(sp)):
        if sp[i] in count:
            count[sp[i]] = count[sp[i]] + 1
        else:
            count[sp[i]] = 1

countOfLoop = 0
top10 = []
for k,v in sorted(count.items(), key = lambda x:x[1], reverse = True):
    countOfLoop += 1
    if (countOfLoop < 11):
        top10.append(str(v) + " " + k)
        print(v,k)

#diff = difflib.unified_diff(top10,open(comp_file).read().strip().split("\n"))
#for i in diff:
#    print(i)

    
