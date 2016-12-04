'''Exercise 6.3
The following program counts the number of times the letter 'a' appears
in a string:

word ='banana'
count = 0
for letter in word:
    if letter =='a':
        count = count + 1
print(count)

Encapsulate this code in a function named count, and generalize it
so that it accepts the string and the letter as arguments.'''

def count(word,letter):
    count = 0
    for x in word:
        if x == letter:
            count = count + 1
    return count
    
print(count('banana', 'a'))
