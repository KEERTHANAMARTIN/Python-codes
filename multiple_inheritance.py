# Diamond Problem
class A:
    def method(self):
        print("Method of class A ")
class B(A):
    def method(self):
        print("Method of class B ")
class C(A):
    def method(self):
        print("Method of class C ")
class D(B,C): # we have to give both variables because the D goes to both B and C
    pass

d=D()   # creating object is also calling
#b=B()
#c=C()
d.method()
#b.method()
#c.method()


class A:
    def method(self):
        print("Method of class A ")
class B(A):
    pass   # giving pass to B to print c
class C(A):
    def method(self):
        print("Method of class C ")
class D(B,C): # we have to give both variables because the D goes to both B and C
    pass

d=D()   # creating object is also calling
#b=B()
#c=C()
d.method()