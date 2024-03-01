my_list=[1,2,3,4,5,6]
for i in my_list:
    my_list.remove(i)
    print(my_list)
def leap_year(year):
    if (year % 4 == 0 and year % 100 !=0) or (year %400 == 0):
        print("It is a leap year")
def get_days_in_month(month,year):
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
days_in_month = get_days_in_month(month,year)
if days_in_month == -1:
    print("Invalid month ")
else:
    print(f"The number of days in {month}/{year} is: {days_in_month}")


num = [1,2,3]
num.insert(4,3)
print(num)

input=input("Give a name")
vowels="aeiou"
output=""
for x in input:
    if x in vowels:
        if input[input.index(x)+1] == x:
            output=output+x
        else:
            pass
    else:
        output=output+x
        print(output)


number ="zero"
for number in range(10):
    print(number*2)