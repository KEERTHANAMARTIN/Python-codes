from oopsdemo import calculator
class child(calculator):
    num2 = 200

    def __init__(self):
        calculator.__init__(self,10,20)
    def getcompletedata(self):
        return self.num2 + self.num + self.summation()

obj = child()
print(obj.getcompletedata())