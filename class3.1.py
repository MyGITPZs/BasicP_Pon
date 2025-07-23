
print("--------------------------")
sum = 0
round = int(input("จำนวนรอบ :"))
for i in range(1,round+1):
    sum = sum + i
    print("รอบที่ ", i , "ผลรวามคือ ", sum)
print("--------------------------")

while True:
    inp = int(input("input number : "))
    if inp >= 7:
        break