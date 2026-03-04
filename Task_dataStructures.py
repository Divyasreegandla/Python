# list

# fruits=["Apple","Banana","Cherry","Apple","Cherry","Pineapple"]
# fruits.append("Orange")
# fruits.extend(["Mango","Grapes"])
# fruits.insert(1,"Papaya")
# fruits.remove("Apple")
# fruits.pop()
# fruits.pop(2)
# print(fruits.index("Banana"))
# print(fruits.count("Cherry"))
# fruits.sort()
# fruits.reverse()
# # fruits.sort(reverse=True)
# # fruits.clear()
# print(fruits)

#tuple

# colors=("Red","Yellow","Blue","Orange","White","Blue","White",1,2,3,4)
# print(colors.index("Blue"))
# print(colors.count("White"))

# t=1,2,3,4,5,6

# a,b,c,d,e,f=t

# print(d)


#set

# primeNum={2,3,5,7,5,2,7,3,13}
# primeNum.add(11)
# primeNum.remove(3)
# # primeNum.clear()
# print(primeNum)

# set1={1,2,3,4,5,6}
# set2={4,5,6,7,8,9}
# print(set1.union(set2)) #{1,2,3,4,5,6,7,8,9}
# print(set1.intersection(set2)) #{4,5,6}
# print(set1.difference(set2)) #{1,2,3}
# print(set2.difference(set1)) #{8,9,7}

#Dictionary

company={
    "name":"Divya",
    "company":"Stackly",
    "role":"ASE",
    "emp_id":"STK-25",
    "remote":True
}

print(company.keys()) #dict_keys(['name', 'company', 'role', 'emp_id', 'remote'])
print(company.values()) #dict_values(['Divya', 'Stackly', 'ASE', 'STK-25', True])
print(company.pop("role")) #ASE
print(company) #{'name': 'Divya', 'company': 'Stackly', 'emp_id': 'STK-25', 'remote': True}
