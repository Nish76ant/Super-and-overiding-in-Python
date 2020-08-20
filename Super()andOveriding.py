class A:

    classvar1 = "I am in a class variable in class A"

    def __init__(self):
        self.var1 = " am inside class A's constructor"
        self.classvar1 = "instance var in Class A"
        self.special = "Special"


class B(A):

    classvar1 = "i am in class B"

    def __init__(self):
        super().__init__()
        self.var1 = " am inside class B's constructor"
        self.classvar1 = "instance var in Class A"


a = A()
b = B()
#print(b.classvar1)
#print(b.special)
print(b.special,b.var1,b.classvar1)
