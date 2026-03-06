# def abc():
#     print("Hi guys!!!!")
# abc()

# def student(name,age,marks):
#     print("Name: ",name)
#     print("Age: ",age)
#     print("Marks: ",marks)
# student("Karan",21,88)

# def myData(name,id,company,role):
#     print("Name: ",name)
#     print("Id: ",id)
#     print("Company: ",company)
#     print("Role: ",role)
# myData("Sai",101,"Stackly","ASE")    # Correct order
# myData(25,"Sai","Ase","Stackly")    # Wrong order because name cant be 25

# def student1(firstName,lastName):
#     print(firstName,lastName)
# student1(firstName="Divya",lastName="Sree")
# student1(lastName="Sree",firstName="Divya")

# def sumOfDigits(a,b):
#     print(a+b)
# sumOfDigits(a=10,b=15)
# sumOfDigits(b=25,a=10)

# def myFun(x,y=50):
#     print("x: ",x)
#     print("y: ",y)
# myFun(10)

# def myFun(x,y=50):
#     print("x: ",x)
#     print("y: ",y)
# myFun(10,100)

# def multi(*n):
#     mul=1
#     for i in n:
#         mul*=i
#     print(mul)
# multi(1,2,3,4,5)

# def evenOdd(num):
#     if num%2==0:
#         return "Even Number"
#     else:
#         return "Odd Number"
    
# result=evenOdd(int(input()))
# print(result)

# def vote(age):
#     if age<18:
#         return "Not Eligible to vote"
#     else: 
#         return "Eligible to vote"
# voter=vote(int(input()))
# print(voter)