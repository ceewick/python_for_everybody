'''9.1 Write a program that reads the words in words.txt and stores them as
keys in a dictionary.  It doesn’t matter what the values are. Then you can
use the in operator as a fast way to check whether a string is in the
dictionary'''

file = open('romeo.txt')
d = dict()

text = file.read()
filespl = text.split()

for word in filespl:
    d[word] = 0

print(d)

## OR

'''
file = open('romeo.txt')
d = dict()
file = file.read()

for words in file:
    words = file.split()

for word in words:
    d[word] = 0

print(d)
'''
