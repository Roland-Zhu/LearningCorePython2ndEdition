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