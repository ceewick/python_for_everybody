#5.2 Write another program that repeatedly prompts a user for numbers (as
##above) and then computes the maximum and minimum of the numbers instead
##of the average. If the user types 'done', it calculates max and min. If
##user enters anything other than a valid number catch it with a try/except
##and puts out an appropriate message and ignores the number. Enter
##the numbers from the book for problem 5.1 and Match the sample output below.

lar = 0
sma = 0

while True:
    inp = input('number?')
    inp = inp.lower()
    if inp == 'done':
        break
    else:
        try:
            inp = float(inp)
            if inp > lar:
                lar = inp
            if inp < sma:
                sma = inp
        except:
            print('Enter a number mofo!')

print('large =', lar, 'small =', sma)
