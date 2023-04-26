class A:
    def one(self):
        print("1")

    def two(self):
        print("2")

class B(A): # Class B is inheriting from class A
    def three(self):
        print("3")

    def four(self):
        print("4")

# only see objects in A
a1 = A()
a1.one()
a1.two()

b1 = B()
b1.one()
b1.two()
b1.three()
b1.four()
