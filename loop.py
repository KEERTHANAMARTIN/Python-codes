## oops concept
class calculator:
    num = 100
    def getdata(self):
        print("I'm now executing as method in class")

    def __init__(self):  # constructor will come first when a object is created
        # and __init only be the constructor name ,we can't anyother name
        print("I'm called Automatically when object is created")

obj=calculator()
obj.getdata()
print(obj.num)

#using input

class calculator:
    num = 100

    def __init__(self,a,b):## a,b we have to give for a,b as a variables
        self.first=a
        self.second=b
        print("I'm called Automatically when object is created")

    def getdata(self):
        print("I'm now executing as method in class")

    def summation(self):
        print(self.first + self.second + calculator.num)



obj=calculator(20,30)
obj.getdata()
obj.summation()
print(obj.num)

