class Foo(object):
    x = {}

foo1 = Foo()
foo2 = Foo()

foo1.x = 3
foo2.x = 4

print foo1.x
print foo2.x

# See instanceVariable.py

     
