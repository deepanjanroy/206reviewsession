# Very hard
nestedList = [l, l]

l[0] = 5
nestedList[1][1] = 6

print nestedList

y = []
y[:] = nestedList

nestedList[0][0] = 4
y[1] = 5
print y



