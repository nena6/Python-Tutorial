import re

# myfile = open('mbox-short.txt')
# for line in myfile:
#     line = line.rstrip()
#     if re.search('From:', line): #search for lines that contain From:
#         print(line)
#     if re.search('^From:', line):
#         print(line) #search for lines that stat with From:
#     if re.search('^F..m:', line): #search for lines that start with F, followed by any 2 characters, followed by m
#         print(line)
#     if re.search('^From:.+@', line): #search for lines that start with From and have at sign (.+ matches one-or-more, .* matches zero or more characters)
#         print(line)
from docutils.nodes import line

s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\S+@\S+', s) #two-character sequence that matches a non-whitespace character(\S)
print(lst)

myfile = open('mbox.txt')
for line in myfile:
    line = line.rstrip()
    #x = re.findall('\S+@\S+', line)
    #find email address
    x = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]', line) #matches substring that start with a single lowercase, uppercase or number, followed by zero or more non-blank characters, followed by at sign, followed by zeroor more non-blank characters, followed by lowercase or uppercase letter. * or + applies to the single character immediatly to the left
    if len(x):
        print(x)
    #find i.e. X-DSPAM-Confidence: 0.8475
    if re.search('^X-\S*: [0-9.]+', line): #searches for lines that start with X, followed by any non-whitespace characters and :, followed by space, followed by any number(including a decimal). Inside square brackets the period matches actual period (not a wildcard)
        print(line)
    #extract floating number
    y = re.findall('^X-\S*: ([0-9.]+)', line) # parentheses within findall() are ignored when matching but used for extracting a portion of substring that matches regular expression
    if len(y) > 0:
        print(y)
    #extract revision from i.e. Details: https://source.sakaiproject.org/viewsvn/?view=rev&rev=39772
    z = re.findall('^Details:.*rev=([0-9.]+)', line)
    if len(z) > 0:
        print(z)
    #extract time of the day in From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
    w = re.findall('^From .* ([0-9][0-9]):', line)
    if len(w) > 0:
        print(w)

