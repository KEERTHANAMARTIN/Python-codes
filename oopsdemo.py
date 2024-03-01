

#adding 3 numbers

class calculator:
    num = 100

    def __init__(self,a,b):## a,b we have to give for a,b as a variables
        self.first=a
        self.second=b
        print("I'm called Automatically when object is created")

    def getdata(self):
        print("I'm now executing as method in class")

    def summation(self):
        return self.first + self.second + calculator.num


#obj=calculator(20,20)
#obj.getdata()
#print(obj.summation())
#print(obj.num)





