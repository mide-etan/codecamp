#counting pattern

counts = dict()
line = input('enter a line of text: ')

words =line.split()

print('Words:', words)

print('Counting...')

for word in words:
    counts[word] = counts.get(word, 0) + 1
print('counts', counts)
