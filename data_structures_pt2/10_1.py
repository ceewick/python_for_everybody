Exercise 10.1:
Revise a previous program as follows: Read and parse the “From”
lines and pull out the addresses from the line. Count the number of messages
from each person using a dictionary. After all the data has been read, print
the person with the most commits by creating a list of (count, email) tuples
from the dictionary. Then sort the list in reverse order and print out the
person who has the most commits.'''

#note - the bottom one is likely better, but the top was my original and bottom
#was adapted after looking at solutions
#I would like to see someone elses solution bc I still think there is a better way

file = open('mbox-short.txt')
d = dict()
l = list()

for line in file:
    if line.startswith('From '):
        line = line.strip().split()
        email = line[1]
        d[email] = d.get(email, 0) + 1

for email,count in list(d.items()):
    l.append((count,email))
l.sort(reverse = True)

print(l[0][1], l[0][0])

## **OR**
'''
file = open('mbox-short.txt', 'r')
d = {}
##import re
l = []

for line in file:
    if line.startswith('From: '):
        line = line.split()
        email = line[1]
        d[email] = d.get(email, 0) + 1

for email, count in list(d.items()):
    l.append((count, email))
    l.sort(reverse=True)
    
for count, email in l[:1]:
    print(email, count)
'''
