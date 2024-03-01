#List
list=["apple","Orange","pineapple","Strawberry"]
list.append("Kiwi")
print(list)

list.remove("apple")
print(list)

list.sort()
print(list)

list.reverse()
print(list)

square = int(input("Enter the number: "))
square1 = square * square
print(square1)


numsq =[x ** 2 for x in range(1,11)]
print(numsq)

#Merge List

list1 =[1,2,3,4,5,6]
list2 =[7,8,9,10,11]
l =list1+list2
print(l)

#tuples
tup =(2,3,4,6,9,0)
print("First element:", tup[0])
print("Second element:", tup[1])
print("Slice from index 1 to 3:", tup[3:6])
other_tuple = (6, 7, 8)
concatenated_tuple = tup + other_tuple
print("Concatenated tuple:", concatenated_tuple)

def tupfunc(input_tuple):
    return sum(input_tuple)
tup1=(1,2,3,4,5,6)
result = tupfunc(tup1)
print("sum of elements: ",result)

# dictionary
dic = {'mango': 6, 'grapes': 9}

print(dic)

# Adding key values
dic['apple'] = 10
dic['banana'] = 5
dic['orange'] = 8

print("adding key-values:", dic)

# Removing a key value
del dic['banana']

print("removing 'banana' key:", dic)

# Accessing values using keys
print("Value of orange:", dic['orange'])

# Generating a dictionary using dictionary comprehension
sqr_dic = {num: num**2 for num in range(1, 6)}

print(sqr_dic)


# merging dictionary
aa = {'a': 1, 'b': 2}
bb = {'c': 3, 'd': 4}
cc = {**aa, **bb}

print("Merged dictionary:",cc)