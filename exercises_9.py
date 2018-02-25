#Exercise 1

try:
    myfile = open('words.txt')
except:
    print('Something went wrong.')
    exit()

wd = dict()
wl = []
for line in myfile:
    wl += line.split()
    for word in wl:
        wd[word] = word

print(wd)

print(dict(zip(wl, wl)))

#Exercise 2

fname = input('Enter a file name: ')
try:
    myfile = open(fname)
except:
    print('File cannot be opened.')
    exit()

words = []
days = dict()

for line in myfile:
    if not line.startswith('From'):
        continue
    words = line.split()
    if len(words) > 2:
        #print(words, 'Day: ', words[2], 'Length: ', len(words))
        days[words[2]] = days.get(words[2], 0) + 1

print(days)

#Exercise 3

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

print(senders)

#Exercise 4

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

max_value = 0
max_sender = ''
for sender in senders:
    if senders[sender] > max_value:
        max_value = senders[sender]
        max_sender = sender

print(max_sender, senders[max_sender])

#Exercise 5

fname = input('Enter a file name: ')
try:
    myfile = open(fname)
except:
    print('File cannot be opened.')
    exit()

words = []
sender_domains = dict()

for line in myfile:
    if not line.startswith('From'):
        continue
    words = line.split()
    if len(words) > 2:
        domain = words[1].split('@')
        #print(domain)
        sender_domains[domain[1]] = sender_domains.get(domain[1], 0) + 1

print(sender_domains)




