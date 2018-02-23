import time

fhand = open('mbox.txt')
# count = 0
#
# for line in fhand:
#     print('test1')
#     count += 1
# print(count)
for line in fhand:
    #print('test2')
    line = line.rstrip()
    print(id(line))
    if line.startswith('From:'):
        print(line)

#skip uninteresting lines using continue, process interesting lines
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From:'):
        continue
    print(line)

# #search through file (same as string using find)
fname = input('Enter filename: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened: %s' % fname)
    exit()
for line in fhand:
    line=line.rstrip()
    if line.find('@uct.ac.za') == -1:
        continue
    print(line)




