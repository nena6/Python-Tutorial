import string
#Lesson

txt = 'but soft what light in yonder window breaks'
words = txt.split()
t = list()
for word in words:
    t.append((len(word), word))
t.sort(reverse=True)

res = list()
for length, word in t:
    res.append(word)

print(res)

words.sort(reverse=True, key=len) #len bez zagrada - callback
print(words)

#Lesson - print top 10 common words

fhand = open('romeo-full.txt')

counts = dict()

for line in fhand:
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

lst = list()

for key, value in list(counts.items()):
    lst.append((value, key))

lst.sort(reverse=True)

for key, value in lst[:10]:
    print(key, value)
