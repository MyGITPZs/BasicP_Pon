rice = True
spoon = False

print("-----------------")
#NESTED IF
if rice :
    print("มีข้าว")
    if spoon :
        print("มีช้อน")
        print("กินข้าวได้")
    else:
        print("ไม่มีช้อน")
else :
    print("ไม่มีข้าว")

print("-----------------")

for i in range(1 ,5 , 2):
    print("hi", i)

print("-----------------")

box = 0
for i in range(10):
    box = box + i
print(box)



