'''Exercise 10.2:
This program counts the distribution of the hour of the day for each
of the messages. You can pull the hour from the “From” line by finding the
time string and then splitting that string into parts using the colon
character. Once you have accumulated the counts for each hour, print out the
counts, one per line, sorted by hour as shown below.
Sample Execution:
python timeofday.py
Enter a file name: mbox-short.txt
04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1'''

file = open('mbox-short.txt')
d = {} # hour : counts

for line in file:
    if line.startswith('From '):
        time = line.split()
        time = time[5].split(':')
        hour = time[0]
        d[hour] = d.get(hour,0) + 1

l = list()
for hour,counts in d.items():
    l.append((hour,counts))
l.sort()

for hour,counts in l:
    print(hour, counts)  
