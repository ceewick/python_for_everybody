'''Exercise 2: Rewrite your pay program using try and except so that
your program handles non-numeric input gracefully by printing a
message and exiting the program. The following shows two executions
of the program:'''

try:
    inp = input('Hours?')
    hours = float(inp)
    inp = input('rate?')
    rate = float(inp)

    if hours > 40.0:
        check = (rate * 40) + ((hours - 40) * (1.5 * rate))
    else:
        check = rate * hours
    print (check)

except:
    print('Must be number. numeric innput.')
