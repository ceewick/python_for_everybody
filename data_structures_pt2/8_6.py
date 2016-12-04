'''Exercise 8.6:
Rewrite the program that prompts the user for a list of numbers and
prints out the maximum and minimum of the numbers at the end when the user
enters “done”. Write the program to store the numbers the user enters in a
list and use the max() and min() functions to compute the maximum and minimum
numbers after the loop completes.'''

t = list()

while True:
    inp = input('please enter numbers to calculate. Type "done" when finished')
    inp = inp.lower()
    if inp == 'done':
        break
    else:
        try:
            num = float(inp)
            t.append(num)
        except:
            print('please enter number')
print('the max number is {} and the min is {}'.format((max(t)),(min(t))))
