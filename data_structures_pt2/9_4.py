'''Exercise 9.4:
Add code to the above program (9_3) to figure out who has the most
messages in the file.
After all the data has been read and the dictionary has been created, look
through the dictionary using a maximum loop (see Section [maximumloop]) to
find who has the most messages and print how many messages the person has.

Enter a file name: mbox-short.txt
cwen@iupui.edu 5
Enter a file name: mbox.txt
zqian@umich.edu 195

'''

file = open('mbox-short.txt')
d = dict()
lst = list()

for mail in file:
    mail.strip()
    if mail.startswith('From '):
        mail = mail.split()
        mail = mail[1]
        d[mail] = d.get(mail,0) + 1
print(d)

maxim = 0
maxmail = 0

for mail,count in d.items():
    if count > maxim:
        maxim = count
        maxmail = mail
print(maxmail, maxim)
