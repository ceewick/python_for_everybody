'''Exercise 9.2:
Write a program that categorizes each mail message by which day of
the week the commit was done. To do this look for lines that start with “From”,
then look for the third word and keep a running count of each of the days of
the week. At the end of the program print out the contents of your dictionary
(order does not matter).
mbox.txt

Sample Line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Sample Execution:
python dow.py
Enter a file name: mbox-short.txt
{'Fri': 20, 'Thu': 6, 'Sat': 1}'''


file = open('mbox-short.txt')
d = dict()

for line in file:
    if line.startswith('From '):
        word = line.split()
        day = word[2]
        if day not in d:
            d[day] = 1
        else:
            d[day] += 1
print(d)

d[day] = day.get(day, 0) + 1

## OR'''

file = open('mbox-short.txt')
d = dict()

for line in file:
    if line.startswith('From '):
        word = line.split()
        day = word[2]
        d[day] = d.get(day,0) + 1
print(d)
'''
