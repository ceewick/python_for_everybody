'''3.3 Write a program to prompt the user for a score using input.
Print out a letter grade based on the following table:
Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
If the user enters a value out of range, print a suitable error message and
exit. For the test, enter a score of 0.85.'''

##Disclaimer - this code not as efficient as could be

try:
    inp = input('what score?')
    score = float(inp)

    if score >= 0.9:
        score = 'A'
    elif .9> score >= 0.8:
        score = 'B'
    elif .8 > score >= 0.7:
        score = 'C'
    elif .6 > score >= 0.6:
        score = 'D'
    elif 0.0 <= score <= 0.6:
        score = 'F'
    print(score)

except:
    print('Error with input format OR code')
