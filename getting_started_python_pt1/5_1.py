'''Exercise 5.1
Write a program which repeatedly reads numbers until the user en-
ters “done”. Once “done” is entered, print out the total, count, and
average of the numbers. If the user enters anything other than a number,
detect their mistake using try and except
and print an error message and skip to the next number.
Enter a number: 4
Enter a number: 5
Enter a number: bad data
Invalid input
Enter a number: 7
Enter a number: done
16 3 5.33333333333'''

count = 0
total = 0

while True:
    inp = input('Enter #: type "done" to exit the loop and'
                ' calculate the average')
    inp = inp.lower() #Just added now, dont think I knew .lower() at the time
    if inp == 'done':
        break
    else:
        try:
            inp = float(inp)
            count = count + 1
            total = inp + total
        except:
            print('enter a number Mofo!')
average = (total/count)
print('count = ', count, 'total =', total, 'average =', average) 
