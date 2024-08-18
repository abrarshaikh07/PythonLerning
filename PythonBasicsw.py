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
a=open("file.txt","rt")
f=print(a.read())

