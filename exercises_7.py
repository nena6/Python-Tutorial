#Exercise 1

fname = input('Enter a filename: ')

try:
    myfile = open(fname)
    for line in myfile:
        line = line.upper()
        print(line)
except:
    print('Cannot open the file.', fname)
    exit()



#Exercise 2&3

def spam_count(myfile):
    count_lines = 0
    spam_sum = 0
    spam_avg = 0

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
        if count_lines != 0:
            spam_avg = spam_sum / count_lines

    return spam_avg


fname = input('Enter a filename: ')
if fname == 'na na boo boo':
    print('NA NA BOO BOO TO YOU - You have been punk\'d!')
    exit()
try:
    myfile = open(fname)
    spam_average = spam_count(myfile)
    print('Average spam confidence: ', spam_average)

except:
    print('Cannot open the file.', fname)
    exit()





