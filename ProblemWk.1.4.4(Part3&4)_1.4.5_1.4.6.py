class Thing:
    def set(self, v):
        self.x = v
    def get(self):
        return self.x
    def mangle(self):
        self.set(self.get() + 1)
        self.hasBeenMangled = True
    def clone(self):
        result = Thing()
        result.set(self.get())
        return result
    def __str__(self):
        return 'This is a Thing with Value ' + str(self.get())


a = Thing()
a.set(3)
print a
##b = a.clone()
##print b.get()
##a.mangle()
##print a.x, a.hasBeenMangled

def mangled(z):
    result = Thing()
    result.set(z)
    result.mangle()
    return result

##print mangled(1.23).x

def assignThing(Thing1, Thing2):
    Thing1.set(Thing2.get())

##a = Thing()
##a.set(3)
##b = Thing()
##b.set(4)
##assignThing(a,b)
##print a.get(), b.get()


def swapThing(Thing1, Thing2):
    midX = Thing1.get()
    Thing1.set(Thing2.get())
    Thing2.set(midX)

##a = Thing()
##a.set(3)
##b = Thing()
##b.set(4)
##swapThing(a,b)
##print a.get(), b.get()

def sumOfThings(Thing1, Thing2):
    result = Thing()
    result.set(Thing1.get() + Thing2.get())
    return result

##a = Thing()
##a.set(3)
##b = Thing()
##b.set(4)
##print sumOfThings(a,b).get()

def sumOfAllThings(Things):
    result = Thing()
    result.set(sum([t.get() for t in Things]))
    return result

##a = Thing()
##a.set(3)
##b = Thing()
##b.set(4)
##c = Thing()
##c.set(5)
##L = [a, b, c]
##print sumOfAllThings(L).get()


