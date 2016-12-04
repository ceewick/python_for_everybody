'''Exercise 9.5:
This program records the domain name (instead of the address) where
the message was sent from instead of who the mail came from (i.e., the whole
email
address). At the end of the program, print out the contents of your dictionary.
python schoolcount.py
Enter a file name: mbox-short.txt
{'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}'''

file = open('mbox-short.txt')
d = dict()

for line in file:
    if line.startswith('From '):
        line = line.rstrip()
        line = line.split()
        email = line[1]
        domain = email.split('@')
        domain = domain[1]
        d[domain] = d.get(domain,0) + 1
print(d)

##OR
'''
file = open('mbox-short.txt')
d = dict()

for line in file:
    if line.startswith('From '):
        line = line.rstrip()
        domains = line.find('@')
        email = line[domains + 1:]
        domaine = email.find(' ')
        domain = email[: domaine]
        d[domain] = d.get(domain, 0) + 1
print(d)

'''
