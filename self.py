#num = int(input("Enter a number"))
#print("Entered num",num)

#num =64
#num1 = num **0.5
#print(int(num1))

def grade(score):
    if 90 <= score <= 100:
        return 'A'
    if 80 <= score <= 89:
        return 'B'
    if 70 <= score <= 79:
        return 'C'
    if 60 <= score <= 69:
        return 'D'
    else:
        return 'F'

a=int(input("Enter Marks "))
print(grade(a),"This is the grade")


var1 = int(input("Enter a number1 "))
var2 = int(input("Enter a number2 "))
var3 = int(input("Enter a number3 "))
if var1>var2:
    if var1>var3:
        print(var1,"It is the largest number")
else:
    if var2 > var1:
        if var2 > var3:
            print(var2,"it is the largest number")
        else:
            print(var3,"it is the largest number")

def cen(year):
    if year%100==0:
        return 'It is a century'
    else:
        return 'It is not a century'
b = int(input("Enter a year: "))
print(cen(b))