#Exercise 1

s = 'exercise'
i = len(s)-1

while 0 < i < len(s):
    print(s[i])
    i -= 1

for char in s:
    print(char)

#Exercise 3

def count_char(s, char):
    count = 0
    for c in s:
        if c == char:
            count += 1
    return count

print(count_char(s, 'e'))

print(s.count('e'))

#Exercise 5

data = 'X_DSPAM_Confidence:0.8475'

start_index = data.find(':')
print(start_index)
extracted = data[start_index+1:]
print(extracted)
print('Extracted slice %s is %s' % (extracted, type(extracted)))
extracted = float(extracted)
print('Extracted slice %g is %s' % (extracted, type(extracted)))
