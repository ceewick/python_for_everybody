'''Exercise 6.1
Write a while loop that starts at the last character in the string and
works its way backwards to the first character in the string, printing each
letter on a separate line, except backwards.'''

word = input('enter a word')
last = len(word) - 1

while last >= 0:
    letter = word[last]
    print(letter)
    last = last - 1
