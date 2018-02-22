#Exercise 1
#
# count = 0
# total = 0
# average = 0
#
# while True:
#     n = input('Enter a number: ')
#     if n == 'done':
#         break
#
#     try:
#         n = float(n)
#         count += 1
#         total += n
#     except:
#         print('Bad input')
#
# if count != 0:
#     average = total / count
#
# print(count, total, average)

#Exercise 2

count = 0
total = 0
average = 0

smallest = None
largest = None

while True:
    n = input('Enter a number: ')
    if n == 'done':
        break

    try:
        n = float(n)
        count += 1
        total += n
        if smallest is None or n < smallest:
            smallest = n
        if largest is None or n > largest:
            largest = n
    except:
        print('Bad input')

if count != 0:
    average = total / count

print(count, total, average, largest, smallest)
