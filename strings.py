

samp_string = 'This is an important string'

'''print(samp_string[0])
print(samp_string[-1])

print(samp_string[3+5])

print('Length :', len(samp_string))

print(samp_string[8:])

#iterate through char
for char in samp_string:
    print(char) '''


# iterate through strings in pairs
'''for i in range(0, len(samp_string)-1, 2):
    print(samp_string[i] + samp_string[i+1])'''

rand_string = 'This is an important string'

print(rand_string.upper())

print(rand_string.capitalize())

a_list = ['Bunch', 'of', 'random', 'words']
print(' '.join(a_list))

a_list_2 = rand_string.split()
for i in a_list:
    print(i)
