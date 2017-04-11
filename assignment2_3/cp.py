import sys
print(sys.argv)
if len(sys.argv) <3:
    exit(0)
src_name = sys.argv[1]
src = open(src_name,"r")
dest_name = sys.argv[2]
dest = open(dest_name,"w")
dest.write(src.read())

