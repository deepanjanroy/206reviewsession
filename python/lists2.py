print "challenge 1"
l = [1, 2]

newList = l * 2

print newList

print "challenge 2"

a = [1,2,3]
b = []
b[:] = a
a[0] = 5
print a
print b


print "challenge 3"
c = [1,2,3]
d = []
d = c
c[0] = 5
print c
print d

# Harder
nestedList = [l, l]

l[0] = 5
nestedList[1][1] = 6

# print nestedList

y = []
y[:] = nestedList

nestedList[0][0] = 4
y[1] = 5
# print y



