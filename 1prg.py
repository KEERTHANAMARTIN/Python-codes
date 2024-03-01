#print("Hello World")

#Demo = 1234
#print(Demo)

#DemoClass = "2u344" # This is called Camel Case because D and C are caps
#print(DemoClass)

#_Demo1 = 123
#print(_Demo1)

#12Demo=2333
#Print(12Demo) # Error because the variable name starts with number

#Demo21 =1234
#print(Demo21)

#Demo = 1
#Demo = 2
#print(Demo) # the lastest variable value

#Demo = 1
#D =2
#print(Demo+D)

#No = (1,2,3,4,5)
#print(No)

#No = (1-5,51-9,33-8)
#print(No)

#Demo =123
#Demo1 =345
#Demo3 ="Keerthi"
#Demo2 =4667
#print(Demo,Demo1,Demo3,Demo2)

#Demo =123
#Demo1 =345
#Demo3 ="Keerthi"
#Demo2 =4667
#print(type(Demo,Demo1,Demo3))

#Demo =123
#Demo1 =345
#Demo3 ="Keerthi"
#Demo2 =4667
#print(type(Demo),type(Demo1),type(Demo3),type(Demo2))

#Demo = 133
#print(type(Demo))

#sal =200000
#New_sal = float(sal)
#print(New_sal)

#sal=200000
#print(float(sal))

#sal=80.94
#print(int(sal))

#8/01/24 ---> String place holder

#pgm = "Python is a Programming Language"
#print(pgm,"and Easy to learn")
#print('{} and easy to learn'.format(pgm))   #----> (.format)-this is called string holder/place holder

#Pgm = "string is one of the python's data type"
#print(Pgm)

#Pgm = 'string is one of the python\'s data type'
#print(Pgm)

#a= 2<3
#b=5>2
#c=a and b
#print(c)

#a= 2<3
#b=5<2
#c=a and b
#print(c)

#a= 2<3
#b=5>2
#c=a or b
#print(c)

#a= 2<1
#b=5<2
#c=a or b
#print(c)

#1st chapter String
#stringname = "Keerthi" or 'Vivi'

#fruit ="Apple"
#print(len(fruit))
#print(fruit[-2])
#print(fruit[-3])

# UPPERCASE:

#Fruit= ("i love apple")
#print(Fruit.upper())
#print(Fruit.lower())

#pgm =" Python is easy "
#print(pgm.replace(" easy "," Powerful "))
#print(pgm[0:6])
#print(pgm[9:14])
#print(pgm[-5:]) # after -5 everything will return
#print(pgm[:-5]) # before -5 everything will return


                            #10/01/2024 ---> List,Tuples,Dictionary



#fav_fruits =["apple","Orange","pineapple","Strawberry"]
#print(fav_fruits)
#print(fav_fruits[1])
#fav_fruits[1] ="Kiwi"  # if we want to chane orange to kiwi, we have to give like this
#print(fav_fruits)

#fav_fruits.append("Gova") # Gova will be added to the list at the last
#print(fav_fruits)

#fav_fruits.insert(1,"Dragon Fruit")  # insert dragon fruit in 2nd order
#print(fav_fruits)

#fav_fruits.remove("apple")
#print(fav_fruits)

#fav_fruits.sort()
#print(fav_fruits)

#num = ["4","6","56","32","76"]   # order will be different, first the Caps, Small,then numbers
#num.sort()
#print(num)

#num1=[1,5,8,4,24,88]
#num1.sort()
#print(num1)

#names = ["Keerthi","Poova","Swathi","chennai"]
#names.sort()
#print(names)

#fav_fruits.reverse()
#print(fav_fruits)

#print(fav_fruits.pop())  # it will show and delete it from the list

#print(fav_fruits.pop(2))  # to delete particular value , give the index number to delete it

                            # Tuples

#wardates=(1913,1945)
#print(wardates)

#wardates[1]=1988
#print(wardates)          # error tuples does update

#wardates.reverse()
#print(wardates)          # error tuple does not reverse

#del(wardates)


                           # Dictionary

#cam ={"Sony":500,"Nikon":799,"Canon":654}
#print(cam)

#cam["Nikon"]=900
#print(cam)

                    #------- 11/01/24 ---------

#print(cam.keys())
#print(cam.values())

#copycam=cam.copy()
#print(copycam)

#del cam["Sony"]
#cam.clear

#print(cam)


          #-----------------31/01/24-------------------------#
my_set={1,2,3,4,5}
print(my_set)
#---------add a set-----
my_set.add(6)
print(my_set)

#----------Removing an element from a set
my_set.remove(3)
print(my_set)

#--------set operator-
set_1={1,2,3,4,5,6}
set_2={5,6,7,8,9}
union_set=set_1.union(set_2)
print(union_set)
intersection_set=set_1.intersection(set_2)
print(intersection_set)

set_difference=set_1.difference(set_2)
print(set_difference)
print(2 in set_1)
print(9 in set_1)

original_set={1,2,3,4,5}
print("original_set:",original_set)

#----------convert the set to list and convert it back to set

reversed_set=set(reversed(list(original_set)))
print(reversed_set)

list=list(original_set)
list.reverse()
reversed_set = set(list)
print(reversed_set)