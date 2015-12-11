foo = 42
def crazyScope():
    foo = 45
    print foo

print foo 

crazyScope()

print foo

for i in range(4):
    foo = i

print foo

