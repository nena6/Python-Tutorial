#Exercise 1

test1 = [1, 2, 3, 4]

def chop(t): #Modifies original list to chop the first and the last element
    t.pop(0)
    t.pop(-1)
    return None

chop(test1)
print(test1)

test2 = [1, 2, 3, 4, 5, 6, 7, 8]

def middle(t): #Returns a new list that contain all but the first and the last element
    return t[1:-1]

new_list = middle(test2)
print(new_list)

#Exercise 4

myfile = open('romeo.txt')

word_list = []

for line in myfile:
    word_list += line.split()
    #word_list.extend(line.split())

word_list.sort()

print(word_list)

#Exercise 5

myfile2 = open('mbox-short.txt')

count_from = 0
senders = []
for line in myfile2:
    if not line.startswith('From:'):
        continue
    count_from += 1
    sender = line.split()[1]
    print(sender)
    senders.append(sender)

print('There were %d lines in the file with From as the first word.' % count_from)
print(senders)

#Exercise 6

number_list = []

while True:
    number = input('Enter a number: ')
    if number == 'done':
        break
    try:
        number = float(number)
        number_list.append(number)
    except:
        print('Bad input.')
        continue

print(number_list)

if len(number_list) > 0:
    print('Maximum: %g' % max(number_list))
    print('Minimum: %g' % min(number_list))
else:
    print('Empty list.')

