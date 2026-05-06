while True:
# We are asking for budget
    budget = input("Please, Enter the Total Budget \n: ")
    try:
        budjet = float(budget)
        break
    except:
        print("Enter only number ")
    # successfully converted budget into float
        
# askingg for price of 1 chip
while True:
    cost = input("Please, Enter cost of single chipset \n: ")
    
    try:
        cost = float(cost)  # successfully converted single chip price into float
    
        o = ( budjet / cost )
        print("Total number of chipset you can perchase is:" ,int(o))
        # Total number chipsets you can buy with the current budget 
        break

    except ValueError:
        print("Please, Enter numbers only")
    except ZeroDivisionError:
        print("Please, Enter non zero number")
    except ValueError:
        print("Enter valid input")



    




    


