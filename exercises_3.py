import sys
#Exercise 1&2
try:
    hours = input('Enter Hours: ')
    hours = float(hours)
except:
    print('Error, please enter numeric input.')
    sys.exit()


try:
    rate = input('Enter Rate: ')
    rate = float(rate)
except:
    print('Error, please enter numeric input.')
    sys.exit()

pay = hours*rate
if (float(hours)>40):
    extra_hours = float(hours) - 40
    pay = pay + float(extra_hours)*float(rate)*1.5

print('Pay: ' + str(pay))

#Exercise 3

score = input('Enter the score between 0.0 and 1.0: ')
try:
    score=float(score)
except:
    print('Bad score')
    sys.exit()

if (score >= 0) and (score <= 1):
    if (score >= 0.9):
        grade = 'A'
    elif (score >= 0.8):
        grade = 'B'
    elif (score >= 0.7):
        grade = 'C'
    elif (score >= 0.6):
        grade = 'D'
    else:
        grade = 'F'
else:
    grade = 'Bad score'
    
print(grade)