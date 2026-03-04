# a="Hello World"
# print(a[-3])

# a="hello guys!!!!" 
# print(a[-2:-4)
# print(a[6:])
# print(a[:6])
# print(a[2:7])
# print(a[::-1]) #reverse the output

#List

# list1=[1,2,3,4,"Hello","Hi",True,False,22,33,44,[22,33,44]]
# print(list1)
# print(len(list1))
# print(list1[4])
# print(list1[3:7]) 
# print(list1[0:7:2])

# list1[3]+=2
# print(list1)
# print(len(list1))

# list2=[213,234,234,234,3,5,234]
# list2.append([3,4,5])
# list2.append("Hello")
# list2.extend([5,6,7,8])
# list2.append("Hello")
# list2.extend("Hello")
# list2.insert(4,"hello")
# list2.remove(234)
# list2.pop()
# list2.clear()
# list2.sort() # asending
# list2.sort(reverse=True) # decending
# list2.reverse()
# print(list2[::-1])
# list2.reverse()
# print(list2)
# print(len(list2))

# print(list2[-4:-2])
# print(list2[-2:-4])
# print(list2.count(234))
# print(list2.index(234))

#Tuple

# tup1=(1,2,3,4,3,2,1,"Hello","Hi")
# tup1[3]=44   #not possible error
# print(tup1.index("Hello"))
# print(tup1.index("Hello world"))  #error
# print(tup1[3])
# print(tup1.count(2))

# tup2=1,2,3
# print(tup2)

# person1="vijay",51,"GOAT",68

# name=person1[0]
# age=person1[1]

# name,age,lastMovie,noOfMovies=person1

# print(age)

# Set 

set1={1, 2, 3, 5, 6, 7, 8, 10}
set2={7,8,9,10,11,12,13}

# print(set1[2]) #error
# set1.add(10)
# set1.remove(8)
# set1.clear()

# print(set1.union(set2))
# print(set1.intersection(set2))
# print(set1.difference(set2))
# print(set2.difference(set1))

# for i in set1:
    # print(i)


# Dict 

# studentDetail={
#     "name":"Prem",
#     "class":12,
#     "allClear":True
# }

# print(studentDetail["name"])
# studentDetail["class"]=11
# studentDetail["mark"]=498

# print(studentDetail.keys())
# print(studentDetail.values())
# studentDetail.pop("allClear")
# print(studentDetail)

# for i in studentDetail:
#     print(studentDetail[i])

# personDetail={
#     "name":"Vijay",
#     "age":51,
#     "lastMovie":"Beast",
#     "noOfMovies":68,
#     "favMovies":[
#         "Master",
#         "Mersal",
#         "Bigil",
#         "Sarkar"
#     ],
#     "lastmovieDetail":{
#         "name":"Beast",
#         "director":"Nelson",
#         "releaseDate":"13th April 2022"
#     }
# }
# print(personDetail["favMovies"][2])