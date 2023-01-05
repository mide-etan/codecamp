xfile = open('mbox.txt')

count = 0
for line in xfile:
    count += 1
    print('line count', count)

# THhis is to print lines that only has @uct
fhand = open(mbox.txt)
for line in fhand:
    line = line.rstrip()
    if not @uct in line:
        continue
    print(line)
