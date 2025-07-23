monster = 100
wood = 10
bow = 20
gun = 30
rounds = 0

while True:
    fight = int(input("1 , 2 : "))
    if fight == 2:
        break
    elif fight == 1:
        rounds = int(input("ตีกี่รอบ : "))
        for i in range(rounds):
            print("1.wood")
            print("2.bow")
            print("3.gun")
            choose = int(input("1 ,2 ,3 :"))       
            monster = monster - choose
            print(monster)
            if 0 > monster < 0  :
                monster = 20
                print("you lose")


    else :
        print("เลือกใหม่")

