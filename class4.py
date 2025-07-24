# #def hello():
# #    print("Hello World")
# #
# #
# #hello()
# #print("--------------------")
# #
# #def add(a,b):
# #    print(a+b)
# #    print(a*b)
# #
# #add(10,4)
# #print("-------------------")
# #
# #x = int(input("number :"))
# #y = int(input("number :"))
# #add(x,y)
# #print("--------------------")

# print("------------------")

# def me(sname):
#     print("My name is", sname)
#     tellage()

# def tellage():
#     tell = input("How old are you : ")
#     print("คุณอายุ : ", tell)

# me("pon")
# print("------------------")

# def spam(x):
#     for i in range(5):
#         print(x)

# spam("Hello")

# print("------------------")

print("------------------")
#list
#box = ["x","y","z",1,2,3]

# print(box[4] + box[5])
# box[4] = 8
# print(box[4] + box[5])

# box[4] = "test"
# print(box[4])
# print("------------------")

# box.append("a")
# box.append(8.4)
# print(box)

# box.pop(2)
# box.pop(4)
# print(box)
# print("------------------")

# for i in box:
#     if i == 2:
#         print(i)
#     else:
#         print("not found")
    
# print("------------------")

# dic = {
#     "A" : 80,
#     "B" : 70,
#     "C" : 60
    
# }
#print(dic["B"])

# dic["A"] = 10

# print(dic)

# dic["D"] = 50
# print(dic)

# print("--------------------")

# student = [
#     {"name": "A", "ID": 1, "score": 10},
#     {"name": "B", "ID": 2, "score": 20}
# ]

# for i in student:
#     print(i["score"])

print("--------------------")

# students = [
#     {"name": "Pangpon", "money": 400},
#     {"name": "Ton", "money": 1000}

# ]
def check(list):
    for ppl in list:
        if ppl["money"] > 500:
            print(ppl["name"], "เงินมากกว่า 500")
        else:
            print(ppl["name"],"เงินน้อยกว่า 500")

students = [
    {"name": "Pangpon", "money": 400},
    {"name": "Ton", "money": 1000},
    {"name": "A", "money": 999},
    {"name": "B", "money": 40},
]
        
check(students)