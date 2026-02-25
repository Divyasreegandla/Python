# # print("Hello World, Welcome to Python")

# # num=10 #varaible declaration can start with letters
# # _a=20  # _ can be used at starting
# # print(_a)
# # a_b=30 # _ can be used to seperate two wods
# # print(a_b)

# #  #var=20 
# # #  $salary=4
# # # 11num=34
# # # var 1=45
# # '''space cannot be used at the starting
# # it throws an error
# #  '''
# # Python=1
# # print(Python)

# # var1=9
# # print(var1)
# #-------------------------------
# #int

# a=100
# num_data=20

# #float

# b=20.5/num_data
# print(b)

# #string

# name="Divya"
# name1="Sree"
# fullname="My name"+" "+"is "+name+" "+name1 # cancatenation
# print(fullname)
# print("I am "+"working in Stackly"+" "+"as a Associate Software Engineer")

# #boolean

# c=5
# d=6
# print(a>b)
# print(a==b)

# #Type casting
# # -----------------------

# age=25
# print("i am "+str(age)+"years old")

# amount=299.9
# print(int(amount))

# num="60"
# print(int(num))
# print(float(num))

# print(bool(num))
# print(bool(amount))
# print(bool(0))
# print(bool(""))

#Operators
# a=26
# b=39
# # Addition ---> +
# print(a+b)
# # Subtraction ---> - 
# print(a-b)
# # Multiplication ---> *
# print(a*b)
# # Division ---> /
# print(a/b)
# # Floor Division ---> //
# print(a//b)
# # Modulus ---> % (reminder)
# print(a%b)
# # Exponentiation ---> ** 
# print(a**b)

# Comparison Operators (Boolean)
# --------------------

# a=25
# b=30
# # == equal to
# print(a==b)
# # != not equal to
# print(a!=b)
# # < lesser than 
# print(a<b)
# # > greater than
# print(a>b) 
# # <= less or equal to
# print(a<=b)
# # >= greater or equal to
# print(a>=b)

# Logical Operators
# ------------------

# a=True
# b=False
# # AND --> and 
# print(a and b)
# # OR --> or
# print(a or b)
# # NOT --> not 
# print(not a)
# print(not b)

# # Assignment operators:

# # = assign
# a=20
# # += add and assign
# a+=5
# print(a)
# # -= a sub and assign
# a-=5
# print(a)
# # *=
# a*=5
# print(a)
# # /=
# a/=5
# print(a)
# # //=
# a//=5
# print(a)
# # %=
# a%=5
# print(a)
# # **=
# a**=5
# print(a)

# Bitwise Operator

# # and---> &
# print(5&12)
# # or--> |
# print(5|12)
# # x-or ---> ^
# print(5^12)
# # not --> ~
# print(~12)
# # right shift --->  >>
# print(4>>2)
# # left shift---> <<
# print(4<<2)


#Membership operators

# name="Divya"
# print('i' in name)   #true
# print('ya' in name)   #true
# print('a ' in name)    #false
# print('p' in name)   #false

# name="Divya Sree"
# print("iv" not in name)   #false
# print("aS" not in name)     #true

#Identity operators

# a=10
# b=20
# print(a is b)   # false
# print(a is b-10)  #true

# a=15
# b=25
# print(a is not b) #true
# print(b is not a)   #true
# print(a+10 is not 50-b)    #false


# ******************************************************************

# Loops


# N=int(input("Enter a number: "))
# i=1
# a=i
# while i<=N:
#     print(i)
#     i+=1
# print("The Numbers from ",a,"to ",N,"printed successfully using while loop....!")

# for i in range(1,11):
#     print(i)
# print("The Numbers from 1 to 10 printed successfully using for loop....!")

# for i in range(1,21):
#     if i%2==0:
#         print(i)
# print("The Even numbers from 1 to 20 are printed successfully using for loop....!")

# for i in range(2,21,2):
#     print(i)
# print("The Even numbers from 1 to 20 are printed successfully using for loop....!")



# for i in range(1,10):
#     if i==5:
#         break
#     print(i)
# print("Executed Successfully....!")
# print("Loop stopped at i==4 because when i==5 condition",
#          " is satisfied and break is used it comes out of the loop")

# for i in range(1,10):
#     print(i)
#     if i==5:
#         break
# print("Executed Successfully....!")

# i=0
# while i<10:
#     if i==5:
#         break
#     print(i)  
#     i+=1 
# print("Executed successfully ,it breaks when i=5")


# for i in range(1,15):
#     if i==9:
#         continue
#     print(i)
# print("Loop executed, it skips 9")

# i=0
# while i<10:
#     i+=1
#     if i==7:
#         continue
#     print(i)
# print("Executed Successfully, it skips 7")