#Exercise 1
import re

# myfile = open('mbox.txt')
#
# regex = input('Enter a regular expression: ')
#
# matches = 0
# for line in myfile:
#     if re.search(regex, line):
#         matches += 1
# print('mbox.txt had %d lines that matched %s' % (matches, regex))

#Exercise 2

fname = input('Enter file: ')

try:
    myfile2 = open(fname)
except:
    print('Something went wrong with opening the file.')
    exit()

sum = 0
count = 0
for line in myfile2:
    x = re.findall('New Revision: ([0-9]+)', line)
    if len(x) > 0:
        sum += int(x[0])
        count += 1
print(sum/count)

