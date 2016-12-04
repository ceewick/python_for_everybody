'''    ##Exercise 10.3: 116 for string.translate
Write a program that reads a file and prints the letters in decreasing order
of frequency. Your program should convert all the input to lower case and
only count the letters a-z. Your program should not count spaces, digits,
punctuation, or anything other than the letters a-z. Find text samples from
several different languages and see how letter frequency varies between
languages. Compare your results with the tables at
wikipedia.org/wiki/Letter_frequencies.'''

## Note - In first example, I used "Regular Expressions" module which will be
discussed in next chapter 11. Below that is a solution using the "string"
module

inp = input('Enter file name -ex - "mbox-short.txt"')
file = open(inp, 'r')
d = {}
t = ()

import re #regular expression module)

for x in file:
    y = x.lower()
    letter = re.findall('[a-z]', y)
    for l in letter:
        d[l] = d.get(l, 0) + 1
s = []        
for letter, count in list(d.items()):
    s.append((count, letter))
s.sort(reverse=True)

for count, letter in s:
    print(letter, count)

## OR 

from string import digits, punctuation, whitespace

inp = input('Enter file name -ex - "mbox-short.txt"')
file = open(inp, 'r')
letters = dict()

remove_digits = str.maketrans('', '', digits)
remove_punc = str.maketrans('', '', punctuation)
remove_space = str.maketrans('', '', whitespace)

for line in file:
    line = line.translate(remove_digits)
    line = line.translate(remove_punc)
    line = line.translate(remove_space)
    line = line.lower()
    word = line.split()
    for letter in line:
        letters[letter] = letters.get(letter,0) + 1

letterlist = []
for letter, count in letters.items():
    letterlist.append( (count, letter) )
letterlist.sort(reverse=True)

for count, letter in letterlist:
	print (letter, count)      

    
