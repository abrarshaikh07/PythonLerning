#     # # # ## l=[1,2,3]
#     # # # # # print(l)
#     # # # # # print(l.append(4))
#     # # # # # print(l)
#     # # # # # print(l[0])
#     # # # # # m=[8,5,9,4,6]
#     # # # # # print(m)
#     # # # # # (m.sort())
#     # # # # # print(m)
#     # # # # # (m.sort(reverse=True))
#     # # # # # print(m)
#     # # # # # oreder for character list
#     # # # # oc=['apple','orange','banana']
#     # # # # print(oc)
#     # # # # oc.sort()
#     # # # # print(oc)
#     # # # # oc.sort(reverse=True)
#     # # # # print(oc)
#     # # # #
#     # # # #reverse list
#     # # # # rl=[1,2,3,4,5]
#     # # # # print(rl)
#     # # # # rl.reverse()
#     # # # # print(rl)
#     # # # # # insert in list'
#     # # # # il=['a','b','c','d']
#     # # # # print(il)
#     # # # # il.insert(0,1)
#     # # # # print(il)
#     # # #
#     # # # #index method
#     # # # im = ['a', 'b', 'c', 'd']
#     # # # print(im)
#     # # # p=im.index('b')
#     # # # print([p])
#     # # #
#     # # # #remove method //remove target attribute when it comes first only l
#     # # # rm=[1,2,3,5]
#     # # # print(rm)
#     # # # rm.remove(2)
#     # # # print(rm)
#     # #
#     # # # pop method ; to delete attribute according to index
#     # # pm=[2,59,7,9]
#     # # print(pm)
#     # # pm.pop(0)
#     # # print(pm)
#     # # # copy method
#     # # x=pm.copy()
#     # # print(x)
#     # #
#     # #
#     # # #reverse method
#     # # y=x.reverse()
#     # # print(x)
#     # #
#     # # extend method
#     # x=[1,2,3,4]
#     # y=[5,6,7,8,9]
#     # x.extend(y)
#     # print(x)
#     #
#     # add method
# # tupels
# # tu=(1,2,3)
# # print(tu)
# # print(tu.count(1))
#
# # print("Enter your favourite movies name: ")
# # a=[input(str("First: "))]
# # b=[input(str("Second: "))]
# # c=[input(str("Third: "))]
# # print(type(a))
# # d=list(a+b+c)
# # print(d)
# # print(a)
# # print(b)
# # print(c)
# # a.append(b)
# # print(a)
# # print(d)
# # a=[1,2,30]
# # b=[464,5456,5]
# # print(a+b)
#
# # merging list using apend
# # movie=[]
# # mov=input("Enter movie name")
# # movie.append(mov)
# # mov=input("Enter movie name")
# # movie.append(mov)
# # mov=input("Enter movie name")
# # movie.append(mov)
# # print(movie)
# #
# # a=[]
# # a.append(input("Enter movie move name: "))
# # print("\n*******************************")
# # a.append(input("Enter movie move name: "))
# # print("\n*******************************")
# # a.append(input("Enter movie move name: "))
# # print(a)
# #
# # b=list[a.reverse()]
# # print(b)
# # print(type(b))
#
# # a=len(input("enter "))
# # print(a)
# #
#
#
# # a.rever
# # print(a)
# #
# # a=[1,2,1]
# # # a=[input("Enter a list")]
# # b=a.reverse()
# # print(b)
# #
# # if a==b:
# #     print("this is palindrome list")
#
# # # list copy
# # a=[]
# # a.append(input("Enter movie move name: "))
# # print("\n*******************************")
# # a.append(input("Enter movie move name: "))
# # print("\n*******************************")
# # a.append(input("Enter movie move name: "))
# # print(a)
# # copy_a=a.copy()
# # copy_a.reverse()
# # if copy_a == a:
# #     print("This is palindrome list"
# #           "")
#
# # a=[1,2]
# # a.reverse()
# # b=a
# #
# # print(b)
#
# #dict program
#
# # dic={}
# # a=input("enter subject name :")
# # b=input("Enter Marks ")
# # dic[a]=b
# #
# # a=input("enter subject name :")
# # b=input("Enter Marks ")
# # dic[a]=b
# # a=input("enter subject name :")
# # b=input("Enter Marks ")
# # dic[a]=b
# #
# # print(dic)
#
# # set program
# #
# # s=set()
# # print(type(s))
# # a=input("Enter")
# # s.add(a)
# # a=input("Enter")
# # s.add(a)
# # a=input("Enter")
# # s.add(a)
# # print(s)
#
# #tupel program
# # s=()
# # print(type(s))
# # a=input("Enter")
# # b=input("Enter")
# #
# # c=input("Enter")
# # s=(a,b,c)
# # print(s)
#
# #set and tuple
# # a={
# #     ('subject', 9),
# #     ('fdfs',10)
# #
# #
# # }
# # print(a)
# # print(type(a))
#
# #list calling
# # a=[1,2,3,4,5]
# # print(a)
# # print(a[0])
# # m=[7]
# # x=a.__add__(m)
# # print(x)
#
# #tuple calling
# # a=(1,2,3,4)
# # print(a)
# # print(a[1],)
# # n=(10,11)
# # print(type(n))
# # y=a.__add__((n))
# # print(y)
#
# #dict calling
# # dict={}
# #
# # user=input("Enter your name: \n")
# # add=input("Enter your address: \n")
# # dict.update({user: add})\
# #
# # user=input("Enter your name: \n")
# # add=input("Enter your address: \n")
# # dict.update({user: add})\
# #
# #
# #
# # print(dict)
# # print(dict["Abrar"])
# # print(type(dict))
#
# # set calling
# # a=set()
# # print(type(a))
# # a.update(input("Enter your name: \n"))
# # print(a)
# # a.add("abrar")
# # print(a)
#
# # se={'dsfsd','abrar','aman','hasnian'}
# # # se1=set()
# # # se.add("Abrar")
# # # # print(se)
# # print(se)
# # print(type(se))
# # s=[se]
# # print(type(s))
# # print(s[0])
# # print(s)
#
# my_set = {1, 2, 3, 4, 5}
#
# # Iterate over the set
# # for a in my_set:
# #     print(a)
# # if 3 in my_set:
# #     print("3 is in the set")
#
# #loops
# #while
# # count=str(input("Enter your name: \n"))
# # i=1
# #
# # while i  <=5:
# #     print("Happy Birthda Saiyed {} sahab")
# #     i+=5
# #
# i=int(input("Enter any number: "))
#
# while i!=0:
#     print(i)
#     print("\n")
#     i=i*2
#     if i ==100:
#         break
# print(i)

# i=0
# n=1
# print(i) # 0
# print(n) # 1
# while(i<=5):
#     i=i+n # 1
#     n= n+1 # 2
#     print(i) # 1
#
# # 0,1,1,2,3,5...
#
# i = 0
# k = 1
# loop
# l = i + k = 1
#
#
#
#
# #fibonacci
# a=0
# b=1
# print(a)
# print(b)
#
# while b<=100:
#     c= a+b
#     print(c)
#     a=b
#     b=c
#
#
# tup=('abrar','ahamad','aman')
# x='aman'
# i=0
# while i<len(tup):
#     if (tup[i]==x):
#       print(f"fount at  {i}")
#     i+=1
#
# for i in range(1,10):
#     if (i%2==0):
#         continue
#     print(i)

# n=int(input("enter last number "))
# n=n+1
# n=n*n
# n=n/2
# print(n)

# k=int(input("enter number:"))
# sum=0
# for i in range(1,k+1):
#     sum+=i
# print(sum)
# def k():
#     i=int(input("Enter any number: \n"))
#     j=int(input("Entry second number: \n"))
#     print(i+j)
# k()

#avg function
# def avg(a=int(input("enter \n")),b=int(input("enter \n")),c=int(input("Enter\n"))):
#     sum=a+b+c
#     d=sum/3
#     print(d)
#     return d
#
#
# avg()
# n=int(input("Enter number: \n"))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
#     # i+=1
#
# print(fact)

#conver usd to cad
# def converter(usd=int(input("Enter amount in USD\n"))):
#     inr=usd*83
#     print(f"conversion is\n{usd} is equal to {inr}")
#
# converter()

# odd even function




# def number_check(i=int(input("Enter any number:\n"))):

# def num_check():
#     i = int(input("enter number:\n"))
#     while i !=0:
#         if i%2==0:
#             print("This is even number")
#             num_check()
#         else:
#             print("this is odd")
#             return
#         break
# num_check()
# n=1
# for i in n:
#     n=int(input("enter number:\n"))
#     if n%2==0:
#         print("this is even")
#         continue
#     else:
#         print("this is odd")
#         break


# for number in range(1000):  # The loop will iterate up to 1000 times
#     number = int(input("Enter a number:\n"))
#
#     if number % 2 == 0:
#         print(f"{number} is even. Continuing...")
#         continue  # Continue to the next iteration if the number is even
#     else:
#         print(f"{number} is odd. Breaking the loop.")
#         break  # Break the loop if the number is odd



# sum+=n;





# def sum_fn(n):
#     if n<=1:
#         return n
#     return (n+sum_fn(n-1))
#
#
#
# x=sum_fn(n=int(input("Enter")))
# print(x)
# # def sum_funciton():
#     if sum == 0:
#         print(sum)
#     for i in range(fn,ln):
#         if i==ln:
#             print(sum)
#             break
#         else:
#            sum= sum +1
#            i = +1
#         sum_funciton()
#
#
# def name(l,i=0):
#     if (i==len(l)):
#         return
#
#     print(l[i])
#     name(l,i+1)

# k=['abrar','aman','ahamad']ls

# name(k)
# a=open("file.txt","w+")
# a.write("this is a write method which overwrite all the content")
# a.seek(0)
# k=a.read()
# print(k)
# a.close()
# #
# with open("file.txt","r") as a:
#     print(a.read())  # no need to close the file  using this with function
#
# import os   #To delete file
# os.remove("file.txt")


# a=open("practice.txt","+w")
# a.write("Hi everyone \n wxil i/o\n using java\n I like programming in java")
# a.close()

# with open("practice.txt","r+") as f:
#     a=f.read()
#     k=a.replace("java","Python")
#
# with open("practice.txt","w") as f:
#     f.write(k)
# \
# with open("practice.txt","r") as f:
#     k=f.read()
#     j=k.find()
#     print(j)


# x
#
# k=check_for_line()
# print(k)

# with open("practice.txt","r") as f:
#     s=f.read()
#     p=s.len()
#
#     while p is True:
#         word = input("Enter the word you want to search for: ")
#         try:
#             if(word in s):
#                 print("Your word is found")
#                 k=s.find(word)
#                 print(k)
#             break
#         except ValueError:
#             print("Not Found")

# while True:
#
#     try:
#         x=int(input("Enter number: "))
#         break
#     except ValueError:
#         print("it is not int")

# try:
#     with open("practice.txt", "r") as f:
#         s = f.read()
#
#     while True:
#         try:
#             word = input("Enter the word you want to search for: ")
#             if word in s:
#                 print("Your word is found")
#                 k = s.find(word)
#                 print(f"Word found at index: {k}")
#             else:
#                 print("Not Found")
#         except Exception as e:
#             print(f"An error occurred during the search: {e}")
#
#         choice = input("Do you want to search for another word? (yes/no): ").lower()
#         if choice != "yes":
#             break
#
# except FileNotFoundError:
#     print("The file 'practice.txt' was not found.")
# except IOError:
#     print("An I/O error occurred while reading the file.")
# except Exception as e:
#     print(f"An unexpected error occurred: {e}")

# with open("integer.txt", "w+") as f:
#     k=f.write("1,5,75,89,564,56,46,72,92")

# with open("integer.txt", "r") as f:
#     # Read the content of the file
#     data= f.read()
#     num=""
#     for i in range(len(data)):
#         if (data[i]== ","):
#             if int(num) % 2==0:
#                 print(f"THis {num} is even number")
#
#             num=""
#         else:
#               num=num+data[i]
#
# with open("integer.txt", "r") as f:
#      data=f.read()
#      number=data.split(",")
#
#
# for i in number:
#     if (int(i) % 2==0):
#         print(i)
#

#class and objects

# class Demo:
#     name="Student"
#
# obj=Demo()
# print(obj.name)


# class Demo2:
    # # name = "Student"
    # def __init__(self,name,address):
    #     self.n=name
    #     self.add=address
    #
    # #
    # #
    # #
    # # def welcome(self):
    # #     print("Welcome to world")
    # #
    # # def hello(self):
    # #     print(f"Hello {self.n}")
    # #
    # #


# print(obj.self)
# obj=Demo2("abrar","kitchener")
# # obj.welcome()
# # print(obj.n)
# obj.hello()


# class Bank:
#     def __init__(self,accountNo,balance):
#         self.bal=balance
#         self.acc=accountNo
#     def credit(self,amount):
#         self.am=amount+self.bal
#         print(f"{self.am} $ is credited")
#
#     def credit(self,amount):
#         self.bal=amount+self.bal
#         print(f"{amount} $ is credited and balance is {self.bal}")
#
#     def debit(self, amount):
#         self.bal = self.bal - amount
#         print(f"{amount} $ is debited and balance is {self.bal}")
#
#     def getbalance(self):
#         print(f"The Final balance is {self.bal}\n")
#
#
# obj=Bank(int(input("Enter any number:\n")),0)
#
# obj.credit(int(input("how much do you want to credit\n")))
# obj.debit(int(input("how much do you want to debit\n")))
# obj.getbalance()


# deleting  object

# class student_name:
#     def __init__(self,name):
#         self.name=name
# obj1=student_name("Love")
# print(obj1.name)
# del obj1
#
# try:
#     print(obj1.name)
# except Exception as e:
#     print("object has been deleted")

# private and public attribure of class

# class pv:
#
#     def __init__(self):
#         pass
#
#     def __hello(self,name):
#         self.name=name
#         print("Hello from private method {}".format(name))
#     def welcome(self):
#         print("I am gonna call __hello(private method)")
#         self.__hello("love")
#
#
#
# obj_pv=pv()
#
# print(obj_pv.welcome())
# print(obj_pv._pv__hello) # It is technically possobiole but in python we wouldn't do this.

#
# try:
#     obj_pv.__hello("love")
# except Exception as e:
#     print("this is private method")
#     print(obj_pv.welcome())



#
# INHERITANCE


# class car():
#
#     def __init__(self,type):
#         self.type=type
#         print(f"your {self.type}Car is just started")
#     def start(self):
#         print("your car is just started")
#
#
#     def stop(self):
#         print("You stopped the car {}".format(self.i))
#
# class Toyota(car):
#
#     def __init__(self,name,type):
#         super().__init__(type)
#         self.name=name
#
#
# #
# #
# obj=Toyota(input("Enter the car type: \n"),input("Enter the car type\n"))
# # print(obj.type)
#
#
# # print(help(Toyota))
# print(isinstance(obj,car)) # to check attribute whether it is object of class or not
#changes on attribute of class and object

# class person:
#     name="anonumous"
#
#     def changename(self, name):
#         self.name=name
#         print(f"your name is {name}")
#
# obj=person()
# obj.changename(input("Enter name\n"))
# print(obj.name) # will print anonumous

# how to change class name value using object.

# #method 1
# class person:
#     name="anonumous"
#
#     def changename(self, name):
#         person.name=name   #changes is here
#         print(f"your name is {name}")
#
# obj=person()
# obj.changename(input("Enter name\n"))
# print(obj.name) # will print anonumous


#method 3 Creating class method
# class person:
#     name="anonumous"
#
#     # def changename(self, name):
#     #     self.__class__.name=name   #changes is here
#     #     print(f"your name is {name}")
#
#     def changename(cls,name):
#         cls.name=name
#         print(f"your name is {name}")
#
#
# obj=person()
# obj.changename(input("Enter name\n"))
# print(obj.name)
#
#
# class Subjects:
#     def __init__(self, phy, math, che):
#         self.phy = int(phy)
#         self.math = int(math)
#         self.che = int(che)
#         total = self.phy + self.math + self.che
#         avg = total / 3
#         print("Your average grade is: {:.2f}".format(avg))
#
#
# while True:
#
#     obj = Subjects(input("Enter physics marks: "), input("Enter Maths marks: "),
#                input("Enter chemistry marks: "))
#
#     a=input("do you want to calculate more grades?\n")
#     if a=='n':
#         break
#
#



# #property
# class Subjects:
#     def __init__(self, phy, math, che):
#         self.phy = int(phy)
#         self.math = int(math)
#         self.che = int(che)
#
#
#     def perc(self):
#         total =  self.phy + self.math + self.che
#         avg = total / 3
#         print("Your average grade is: {:.2f}".format(avg))
#
#
#
#
# obj = Subjects(90,85,95)
# obj.perc()
# obj.phy=52
# obj.perc()

# Creating complex numbers
# a = 3 + 4j
# b = 5 - 2j
#
# # Accessing the real and imaginary parts
# real_part = a.real  # 3.0
# imaginary_part = a.imag  # 4.0
#
# # Performing operations on complex numbers
# c = a + b  # (8+2j)
# d = a * b  # (23+14j)
# print(c)
# print(d)




#complext number in oops
# class complex:
#     def __init__(self,real,img):
#         self.real=real
#         self.img=img
#     def show(self):
#         print(self.real,"i +",self.img)
#
#     def __add__(self,num2):
#        new_real=self.real+num2.real
#        new_img=self.img+num2.img
#        print(new_real, "i +", new_img)
#        # print(num3)
#        # return  complex(new_real,new_img)
#
#
#
# num1=complex(5,10)
# num1.show()
#
# num2=complex(5,10)
# num2.show()
#
# print(num1+num2)

# num3=num1.add(num2)
# num3.show()




# class grade:
#     def __init__(self,phy,che,math):
#         self.phy=phy
#         self.che=che
#         self.math=math
#         percentage=int((phy+che+math)/3)
#         print(f"your avg is {percentage}")
#
#     @classmethod  #they are alternative constructor.They use if want to provide attribute not in the format of class attribute does.
#     def customformat(cls,phy,che,math):
#         cls.phy=float(phy)
#         cls.che=float(che)
#         cls.math=float(math)
#         return cls(phy,che,math)
# s1=grade(80,89,85)
# s1.customformat(80,89,85)
#

# class Rectangle:
#     number_of_instances = 0  # Class variable to keep track of instances
#
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#         Rectangle.number_of_instances += 1
#
#     def area(self):
#         return self.length * self.width
#
#     @classmethod
#     def from_square(cls, side_length):
#         # Class method: creates a Rectangle with equal sides (a square)
#         return cls(side_length, side_length)
#
#     @classmethod
#     def get_instance_count(cls):
#         # Class method: returns the number of Rectangle instances created
#         return cls.number_of_instances
#
# # Create a rectangle using the regular constructor
# # rect1 = Rectangle(5, 3)
# # print(f"Area of rect1: {rect1.area()}")
# #
# # # Create a rectangle using the class method from_square
# # square = Rectangle.from_square(4)
# # print(f"Area of square: {square.area()}")
# #
# # Get the number of instances created
# print(Rectangle.get_instance_count())
#
#
#


#repr method
#
# class mobile:
#     def __init__(self,brand,year,model):
#         self.brand=brand
#         self.year=year
#         self.model=model
#
#     def __repr__(self):
#         return "mobile({} {} {})".format(self.brand,self .year,self.model)
#
#     # @property
#     def __add__(self, other):
#         return self.year+other.year
#
#     def __sub__(self, other):
#         return self.year-other.year
#
#     def __len__(self):
#         return  len(self.brand)
#
#     def fullname(self,year,brand,model):
#         self.year=year
#         self.brand=brand
#         self.model=model
#
#         return ("{} {} {}").format(year,brand ,model)
#
# mobile_1=mobile("Toyota",2019,"Tundra")
# mobile_2=mobile("Ford",2012,"F-150")
# # print(mobile_1)
# # print(mobile.__repr__(mobile_1))
# # print(repr(mobile_1))
#
# # print(mobile_1+mobile_2)
# # print(mobile_1-mobile_2)
# # print(len(mobile_1))
#
# # print(mobile_1.__add__(mobile_2))   #using property decorator we can call method as an attribute, it will take the updated value\
#
# #setter method
# print(mobile_1.fullname("sdfsf",464,"fdfsd"))




# def greet(x):
#      '''It will print two line and between them it runs one funciton.'''
#      def func():
#         print("Hi There, How are You?")
#         x()
#         print("Thanks for using this function!")
#      return func
# @greet
# def s():
#     print("Salam")
# s()
# print(greet.__doc__) # It will print the lined which are written just below function.They are not comment but they prvide info about fnunciton.




# a=int(input("Enter num 1 \n"))
# b=int(input("Enter num 2 \n"))
# c=int(input("Enter num 3 \n"))
# print(a) if a>b and a>c else  print(b) if b>c else print(c)
#
# import pandas
#
# print(pd.__version__)
#
# while True:
#
#
#     double=lambda  x: x*x
#     print(double(int(input("Enter any number\n"))))
#
#     i=input("do you want to continue\n")
#     if i.lower()!="y":
#         break
#
# a=(1,2,3,4,5,6)
# new_a=tuple(map(lambda x: x*x,a))
# print(new_a)
#


# a=(1,2,3,4,5,6)
# def func(x):
#     return x>=5
# new_a=tuple(filter(func,a))
# print(new_a)


from functools import reduce
import math
print(math.sq   rt(25))
