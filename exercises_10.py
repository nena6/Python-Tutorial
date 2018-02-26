import string
#Exercise 1

fname = input('Enter a file name: ')

try:
    myfile = open(fname)
except:
    print('File cannot be opened.')
    exit()

words = []
senders = dict()

for line in myfile:
    if not line.startswith('From'):
        continue
    words = line.split()
    if len(words) > 2:
        senders[words[1]] = senders.get(words[1], 0) + 1

# def cb(key):
#     return senders[key]

#max_sender = max(senders, key=lambda key: senders[key])
#print(max_sender, senders[max_sender])

sender_list = list()
for sender, count in list(senders.items()):
    sender_list.append((count, sender))
sender_list.sort(reverse=True)
print(sender_list[0][1], sender_list[0][0])

#Exercise 2

fname = input('Enter a file name: ')

try:
    myfile = open(fname)
except:
    print('File cannot be opened.')
    exit()

words = []
hours = dict()

for line in myfile:
    if not line.startswith('From'):
        continue
    words = line.split()
    if len(words) > 5:
        words = words[5].split(':')
        hours[words[0]] = hours.get(words[0], 0) + 1

hours_list = list(hours.items())
hours_list.sort()

for hour,count in hours_list:
    print(hour, count)

#Exercise 3

fname = input('Enter a file name: ')

try:
    myfile = open(fname)
except:
    print('File cannot be opened.')
    exit()

count = dict()
total = 0
for line in myfile:
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        for c in word:
            if c.isalpha():
                count[c] = count.get(c, 0) + 1
                total += 1
# for letter in count:
#     if total > 0:
#         print('Letter: %s %g%%' % (letter, count[letter]*100/total))

letter_list = list()
for letter, cnt in list(count.items()):
    letter_list.append((cnt, letter))

letter_list.sort(reverse=True)

for cnt, letter in letter_list:
    if total > 0:
        print('Letter: %s %g%%' % (letter, cnt*100/total))




