fhand = open('mbox.txt')
# count = 0
#
# for line in fhand:
#     print('test1')
#     count += 1
# print(count)
print(fhand)
for line in fhand:
    print('test2')
    line = line.rstrip() #kako kad je immutable?
    if line.startswith('From:'):
        print(line)

#fhand = open('mbox.txt') #zasto dvije for petlje ne rade istovremeno???? rade kad se ponovno open napravi, a fhand isti????
print(fhand)
#skip uninteresting lines using continue, process interesting lines
for line in fhand:
    print('test3')
    line = line.rstrip()
    if not line.startswith('From:'):
        continue
    print(line)

#measure time for both loops

#search through file (same as string using find)
fname = input('Enter filename: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened: %s' % fname)
    exit() #je li potrebno? razlika od sys.exit()
for line in fhand:
    line=line.rstrip()
    if line.find('@uct.ac.za') == -1:
        continue
    print(line)




