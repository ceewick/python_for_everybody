'''Exercise 4.7
Rewrite the grade program from the previous chapter using a function called
computegrade that takes a score as its parameter and returns a grade as a string'''

def computegrade(score):
    if 1.3 >= score >= 0.9:
        grade = 'A'
    elif .9> score >= 0.8:
        grade = 'B'
    elif .8 > score >= 0.7:
        grade = 'C'
    elif .6 > score >= 0.6:
        grade = 'D'
    elif 0.0 <= score <= 0.6:
        grade = 'F'
    return(grade)

try:
    score = input("what's score? (as a decimal!)")
    score = float(score)
    print(computegrade(score))

except:
    print('Error with input format')
