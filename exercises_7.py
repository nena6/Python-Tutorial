#Exercise 1

# fname = input('Enter a filename: ')
# try:
#     myfile = open(fname)
# except:
#     print('Cannot open the file.', fname)
#     exit()
#
# for line in myfile: #zasto se zali na fname?
#     line = line.upper()
#     print(line)

#Exercise 2&3

fname = input('Enter a filename: ')
if fname == 'na na boo boo': print('NA NA BOO BOO TO YOU - You have been punk\'d!'); exit() #multiple statements in one line
try:
    myfile = open(fname)
except:
    print('Cannot open the file.', fname)
    exit()

count_lines = 0
spam_sum = 0
for line in myfile:
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    count_lines += 1
    spam_index = line.find(":")
    #print(spam_index)
    try:
        spam = line[spam_index+1:]
        spam = float(spam)
        print('Spam confidence value from this line is: %g.' % spam)
        spam_sum += spam
    except:
        print('Something went wrong when searching for number.')
        exit()

if count_lines == 0:
    spam_avg = 0
else:
    spam_avg = spam_sum / count_lines

print('Average spam confidence: ', spam_avg)



