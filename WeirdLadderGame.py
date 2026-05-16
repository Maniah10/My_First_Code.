import random
total_distance = 100
total_steps = 0
     
while True:
    a = input("Lets go (y/n) \n:  ").lower() #ask for input
    if a == 'y':
        pass
    
    if a == 'n':
        print("Okey, Have a good day ")
        exit()
    elif a.isdigit():
        print("Enter y/n only. ")
        continue
    if a != 'y' and a != 'n':
        print("Enter y/n Only")
        continue
              
    

    dice = random.randint(1,6) 
    print(dice)
    # moving forward 
    match dice:
        case dice if dice == 1:
            total_steps = total_steps + dice
            print("Good luck on your jurney")
            total_distance = 100 - total_steps
            print("You have moved", str(total_steps) + str(' steps up until now'))
            print("Still you have to go", str(total_distance) + str(' steps ahed'))
        case dice if dice == 2:
            total_steps = total_steps + dice
            print("Good luck :) ")
            total_distance = 100 - total_steps
            print("You have moved", str(total_steps) + str(' steps up until now'))
            print("Still you have to go", str(total_distance) + str(' steps ahed'))
        case dice if dice == 3:
            total_steps = total_steps + dice
            print("Nice, Good Luck on your jerney :) ")
            total_distance = 100 - total_steps
            print("You have moved", str(total_steps) + str(' steps up until now'))
            print("Still you have to go", str(total_distance) + str(' steps ahed'))
        case dice if dice == 4:
            total_steps = total_steps + dice
            print("Good one :), go rock :D")
            total_distance = 100 - total_steps
            print("You have moved", str(total_steps) + str(' steps up until now'))
            print("Still you have to go", str(total_distance) + str(' steps ahed'))
        case dice if dice == 5:
            total_steps = total_steps + dice
            print("Amezing, You are rocking from the start")
            total_distance = 100 - total_steps
            print("You have moved", str(total_steps) + str(' steps up until now'))
            print("Still you have to go", str(total_distance) + str(' steps ahed'))
        case dice if dice == 6:
            total_steps = total_steps + dice
            print("Supercalifragialisticexpealodotious :o Simply marvelous :) ")
            total_distance = 100 - total_steps
            print("You have moved", str(total_steps) + str(' steps up until now'))
            print("Still you have to go", str(total_distance) + str(' steps ahed'))
            
            


    if total_steps == 9:
        print("Unefortunately you die, due to snake bite :( ")
        print("Please start from the bigining")
        total_steps = 0
    elif total_steps == 15:
        print("due to unknown reason you move two steps back, strange :< ")
        total_steps = total_steps - 2
    elif total_steps == 21:
        print("You fell from cliff and died :( ")
        print("Start from the beginning ")
        total_steps = 0
    elif total_steps == 1:
        print("Something magical is happening , waight what is this ")
        total_steps = 1 + 11
        print("You move 11 steps ahed")
    elif total_steps == 27:
        print("A bathtub fell from above \nyou lost conciousness \nyou accidentally move 3 steps ahed")
        total_steps = 27 + 3
    elif total_steps == 29:
        print("You hit by somthing \nAhaaaaa \nwhtat is this \n.... \n.... \n... \n.... ")
        print("You hit by a cup, and you died on the place :( ")
        print("Please start from the bigining")
        total_steps = 0
    elif total_steps == 31:
        print("You hit by a ****** and *** \n**** ** ** \n*-* ***+*  \n*/9+-/*/*  \n87/*-+965+8 \n***/*-+-*//  ")
        print("\n... \n..... \n87[oj351ht-0q5z \nX'kzq-77 vll-rtp! Gzz'x 4-qnt... pl-1vrrk 0x-z]")
        print("THOSE WERE ALIANS")
        print("Congratulation!!!")
        print("You move 53 steps ahed")
        total_steps = 31 + 53
    elif total_steps == 36:
        print("You saw somthing and started to run backword ")
        print("You move 6 steps backword ")
        total_steps = 36 - 6
    elif total_steps == 48:
        print("You got burn to crisp and died")
        print("Please start from the bigining")
        total_steps = 0
    elif total_steps == 53:
        print("you saw a cycle on the side \nyou stole it \nand you move 10 steps ahed")
        total_steps = 53 + 10
    elif total_steps == 54:
        print("You try to stole bycycle on 53rd step  \nOwener saw it \nYou died ")
        print("Please start from the bigining")
        total_steps = 0
    elif total_steps == 58:
        print("You went rouge, and you passed out")
        print("You are still on the same place")
        total_steps = 58
    elif total_steps == 67:
        print("someone after you \nA man \nChasing you with club in hand \nHe thinks his girlfriend cheated on him & you are the reason \ngirlfriend killed both of you")
        print("Never go after women, UNDERSTAND! ")
        print("Please start from the bigining")
        total_steps = 0
    elif total_steps == 74:
        print("Kr'zzt-8 jx-vmn! Wq-44... yll'k p-trq 9. \nN-vssx 7-k'lp. Gz-bb m'rrt 22-q!")
        print("An beautiful Alian taook you to her home")
        print("Please start from the bigining")
        total_steps = 0
    elif total_steps == 88:
        print("You got hit on your balls \nYou died")
        print("Please start from the bigining")
        total_steps = 0
    elif total_steps == 97:
        print("You hit by a car \nYou died")
        total_steps = 0
        
        

    # Win Condition
    if total_steps >= 100:
        print("Hooooorrryyyyyyy")
        print("Comgratulations!!!!!!")
        print("You rech your destination!!")
        print("You live ever after")
        print("Thak you for Playing my game :)  \nHope you got the worst luck possible :> :> :D")
        break

        
        

        


