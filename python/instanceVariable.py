class Foo(object):
    def __init__(self):
        self.x = {}

foo1 = Foo()
foo2 = Foo()

foo1.x["a"] = "b"
foo2.x["c"] = "d"

print foo1.x
print foo2.x

# Compare with classVariables.py
