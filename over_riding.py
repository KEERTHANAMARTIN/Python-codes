class employee:
    def setnumberofworkinghours(self):
        self.numberofworkinghours = 40
    def displaythenumberofworkinghours(self):
        print(self.numberofworkinghours)

class trainee(employee): # 2nd ------
    def setnumberofworkinghours(self):
        self.numberofworkinghours = 45
        
    def resetnumberofworkinghours(self): # 3rd--------
        super().setnumberofworkinghours() #super takes to the original value


obj=employee()
obj.setnumberofworkinghours()
print("number of working hours: ", end =" ")
obj.displaythenumberofworkinghours()

Trainee=trainee() #2------
Trainee.setnumberofworkinghours()
print("Number of working hours of trainee ", end="")
Trainee.displaythenumberofworkinghours()

Trainee.resetnumberofworkinghours()  #3----------
print("Number of working hours has been reset: ", end=" ")
Trainee.displaythenumberofworkinghours()