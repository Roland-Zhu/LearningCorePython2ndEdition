#!/usr/bin/python
__author__ = 'aladdin'
print 1 + 2 * 4
print 9 % 4
print pow(2, 3)
#a = raw_input('enter a number:')
#print a
#c = raw_input('enter a int:')
#print int(c)
i = 0
while i <= 10:
    print i
    i += 1
for f in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print f,
print
for f in range(11):
    print f,
i = 0
while i in range(11):
    print i,
    i += 1
test = raw_input('enter a number:')
test = int(test)
if test > 0:
    print '+'
elif test == 0:
    print 0
else:
    print '-'
string = raw_input('enter a string:')
counter = 0
while counter < len(string):
    print string[counter],
    counter += 1
print
for k, v in enumerate(string):
    print k, v

li = [2, 3, 4, 5, 5]
print sum(li) / float(5)
i = 1
while i:
    n = int(raw_input('Enter a number between 1-100:'))
    if n <= 100 and n >= 1:
        print('Done')
        i = 0
    else:
        print('Error')