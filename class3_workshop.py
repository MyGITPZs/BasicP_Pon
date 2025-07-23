while True:
    monsterhealth = 100
    Gun = 40
    Sword = 20
    Hand = 10
    revive = False
    choice = int(input("Press 1 to fights monster , Press 2 toexit : "))

    if choice == 1 :
        fight = int(input("How many time did you fight? : "))
        

        for i in range(fight):
            print("1. Gun   (40)")
            print("2. Sword (20)")
            print("3. hand  (10)")
            weapon = int(input("Use your weapon : ")) 

        
            if weapon == 1:
                monsterhealth -= Gun
                print("Deal Damage 40 ", "Monster Health Remaining : ",monsterhealth )
            elif weapon == 2:
                monsterhealth -= Sword
                print("Deal Damage 20", "Monster Health Remaining : ",monsterhealth)
            elif weapon == 3 :
                monsterhealth -= Hand
                print("Deal Damage 10", "Monster Health Remaining : ",monsterhealth)
        
            if monsterhealth == 0 :
                print("Won")
                break
            elif monsterhealth < 0:
                print("revive","monster come back to 20")
                monsterhealth = 20
                revive = True
       
            if revive == False :
                print("You Lose" , monsterhealth)
            elif revive == True:
                print("It's Revive and die")
                revive = False

        if i == fight and monsterhealth > 0:
            break
        else:
            break

    if choice == 2: 
        print("out")
        break
