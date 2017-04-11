import sys
print(sys.argv)
if len(sys.argv) <2:
    exit(0)
file_name = sys.argv[1]
f = open(file_name)
for line in f:
    print(line, end="")

