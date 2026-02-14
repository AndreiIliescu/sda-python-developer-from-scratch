class A:
    def m(self):
        print(f"this is A")


class B(A):
    def m(self):
        print(f"this is B")


class C(A):
    def m(self):
        print(f"this is C")


class D(B, C):
    pass
    # def m(self):
    #     print(f"this is A")

print(D.mro())
o = D()
o.m()
