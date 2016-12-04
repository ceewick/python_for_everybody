'''7.2 Write a program that prompts for a file name, then opens that
file and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475

Count these lines and extract the floating point values from each of
the lines and compute the average of those values and produce an output
as shown below. Do not use the sum() function or a variable named sum in
your solution. When you are testing below enter mbox-short.txt as
the file name (can download file on main page at:
https://github.com/ceewick/python_for_everybody'''

try:
    inp = input('file name? - try "mbox-short.txt" - download on github: ')
    file = open(inp,'r')
except:
    print ('wrong file name - try again')
    exit()

count = 0
average = 0

for line in file:
    if line.startswith("X-DSPAM-Confidence:"):
        count = count + 1
        point = line.find('.')
        point = float(line[point:])
        average = point + average
average = average / count
print ('Average spam confidence: {}'.format(average))
