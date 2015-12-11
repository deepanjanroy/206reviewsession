x = 5

def innocent():
    x = 7
    print x

print x
innocent()
print x

print "###################################"
def icanteven():
    global x
    x = 7
    print x


print x
icanteven()
print x
