'''Chapter 4 - Exercise 6: Rewrite your pay computation with time-and-a-half for
overtime and create a function called computepay which takes two parameters
(hours and rate).

Enter Hours: 45
Enter Rate: 10
Pay: 475.0'''

def computepay(hours,rate):
    if hours > 40.0:
        check = (rate * 40) + ((hours - 40) * (1.5 * rate))
    else:
        check = rate * hours
    return check

try:
    hours = input('Hours?')
    hours = float(hours)
    rate = input('rate?')
    rate = float(rate)
    print(computepay(hours,rate))
except:
    print('Must be numeric input')
