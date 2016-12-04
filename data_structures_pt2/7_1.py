'''7.1 Write a program that prompts for a file name, then opens that
file and reads through the file, and print the contents the file in
upper case. Use the file words.txt to produce the output below'''


file = input('Whats file name?')
testread = open(file,'r')
testread = testread.read()
print (str.upper(testread))
