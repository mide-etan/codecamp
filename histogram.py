counts = dict()
names = ['csev', 'cwen', 'zqian', 'cwen']
for name in names:
    '''if name not in counts:
    counts[name] = 1
    else:
        counts[name] = counts[name] + 1'''
    counts[name] = counts.get(name, 0) + 1
print(counts)


counts = { 'quincy' : 1 , 'mrugesh' : 42, 'beau': 100, '0': 10}
print(counts.get('kris', 0))
