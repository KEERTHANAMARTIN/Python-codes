import math

#1

num =int(input("Enter a number "))
if num >0:
    print(num,"is positive number")
elif num==0:
    print(num,"is a zero")
else:
    print(num,"is a negative number")

#2

num1=int(input("Enter a number "))
if (num1%4==0 and num1%100!=0) or (num1%400==0):
     print(num1,"it is a leap year")
else:
    print(num1,"it is not a leap year")

#3

var1 = int(input("Enter a number1 "))
var2 = int(input("Enter a number2 "))
var3 = int(input("Enter a number3 "))
if var1>var2:
    if var1>var3:
        print(var1,"It is the largest number")
elif var2 > var1 and var2 > var3:
        print(var2,"it is the largest number")
else:
    print(var3,"it is the largest number")


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



#4
pal = str(input("Enter the string "))
rev = ''.join(reversed(pal))
if pal==rev:
    print(pal,"is a palindrome")
else:
    print(pal,"is not a palindrome")

pal1 = str(input("Enter a string: "))
if pal1 == pal1[::-1]:
    print(pal1,"it is a palindrome")
else:
    print(pal1,"is not a plaindrome")

#5
#age = int(input("Enter the age"))
#if age=range(1-10)

#6
tri1=float(input("Enter the value1 "))
tri2=float(input("Enter the value2 "))
tri3=float(input("Enter the value3 "))
s=(tri1 + tri2 + tri3)/2
abc = math.sqrt(s*(s-tri1)*(s-tri2)*(s-tri3))
print("The area of triangle is",abc)

#7
def grade(score):
    if 90 <= score <=100:
        return 'A'
    if 80<= score <=89:
        return 'B'
    if 70 <= score <=79:
        return 'C'
    if 60<= score <=69:
        return'D'
    else:
        return 'F'
a=int(input("Enter Marks "))
print(grade(a),"This is the grade")


#8
def cen(year):
    if year%100==0:
        return 'It is a century'
    else:
        return 'It is not a century'
b = int(input("Enter a year: "))
print(cen(b))

#9

#10
def leap_year(year):
    if (year % 4 == 0 and year % 100 !=0) or (year %400 == 0):
        print("It is a leap year")
def month1(month):
    if month in {1,3,5,7,8,10,12}:
        return 31
    elif month in {4,6,9,11}:
        return 30
    elif month == 2:
        if leap_year(year):
            return 29
        else:
            return 28
    else:
        return -1

month=int(input("Enter the month: "))
year = int(input("Enter the year: "))
days_in_month = month1(month, year)
if days_in_month == -1:
    print("Invalid month ")
else:
    print(f"The number of days in {month}/{year} is: {days_in_month}")
