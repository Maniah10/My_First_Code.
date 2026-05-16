                # Space Freight Smuggler — Cargo management game
                         # Author: Manesh Bhagane
                            # Built: May 2026





max_weight_capacity = 5000                # Max weight capacity

titanium_price = 500                      #}
platinum_price = 1000                     #}  Cost price of this items per Kg
alien_artifacts_price = 5000              #}

titanium_weight = 0                       #}
platinum_weight = 0                       #}  Weiight of each items in kg
alien_artifact_weight = 0                 #}


titanium_cost = 0                        #}
platinum_cost =  0                       #}  Total cost price = weight * price per kg
aliean_artifact_cost = 0                 #}

kg = 'Kg'         
print("---SPACE FREIGHT SMUGGLER SYSTEM ONLINE----")                        


                                        # Selecting what to add
while True:

    while True:
        a = input("\n-----SELECT THE ITEM YOU WANT TO LOAD----- \n1) Titanium \n2) Platinum \n3) Alien Artifact \n4) Total Weight \n5) Availability Status \n6) Reduce/Remove Cargo \n7) Exit System \n:")
        try:
            a = int(a)
            break
        except ValueError:
            print("Select the given options only")
            continue



                                     # Selecting how much to add
                                    # Titanium Block 
    if a == 1:
        while True:
            new_weight = input("Enter The Amount Of Titanium You Want To Load \n: ")
            try:
                new_weight = int(new_weight)
                break
            except ValueError:
                print("Please Enter the Number only")
                continue
        c = str(new_weight) + str(kg)
        print("You want to load",c,"of Titanium")        # Confirming the input
        while True:
            d = input("yes / no \n:").lower()
            if d == 'yes':
                titanium_weight = titanium_weight + new_weight 
                titanium_cost = titanium_weight * titanium_price
                print("Titanium loaded. Total Titanium:", titanium_weight, kg, "($" + str(titanium_cost) + ")")                
                break
            elif d == 'no':
                print("Loading canceled.")
                break # Just breaks this mini-loop, doesn't kill the program!
            else:
                print("Enter yes or no only.")





                            # Platinum Block
    if a == 2:
        while True:
            new_weight = input("Enter The Amount Of Platinum You Want To Load \n: ")
            try:
                new_weight = int(new_weight)
                break
            except ValueError:
                print("Please Enter the Number only")
                continue

        g = str(new_weight) + str(kg)
        print("You want to load",g,"Platinum")       # Confirming the input
      
        while True:
            f = input("yes / no \n: ").lower()
            if f == 'yes':
                platinum_weight = platinum_weight + new_weight
                platinum_cost = platinum_weight * platinum_price
                print("Platinum loaded. Total Platinum:", platinum_weight, kg, "($" + str(platinum_cost) + ")")
                break
            elif f == 'no':
                print("Loading canceled.")
                break
            else:
                print("Enter yes or no only")
                




                                # Aliean Artifact Block
    if a == 3:
        while True:
            new_weight = input("Enter The Amount Of Aliean Artifact You Want To Load \n:")
            try:
                new_weight = int(new_weight)
                break
            except ValueError:
                print("Please Enter the Number only")
                continue
        h = str(new_weight) + str(kg)
        print("You want to load",h,"Aliean Artifact")      # Confirming the input
       
        while True:
            i = input("yes / no \n:").lower()
            if i == 'yes':
                alien_artifact_weight = alien_artifact_weight + new_weight
                alien_artifact_cost = alien_artifact_weight * alien_artifacts_price
                print("Artifacts loaded. Total Artifacts:", alien_artifact_weight, kg, "($" + str(alien_artifact_cost) + ")")
                break
            elif i == 'no':
                print("Loading canceled.")
                break
            else:
                print("Enter yes or no only")
                


                        # Weight Block
    if a == 4:
        total_weight = titanium_weight + platinum_weight + alien_artifact_weight
        print("\n--- CURRENT CARGO ---")
        print("Titanium:", titanium_weight, kg)
        print("Platinum:", platinum_weight, kg)
        print("Artifacts:", alien_artifact_weight, kg)
        print("Current Total Weight is:", total_weight, "/", max_weight_capacity, kg)
       
      


    elif a == 5:
        total_weight = titanium_weight + platinum_weight + alien_artifact_weight
        
        #  The Safety Sensor
        if total_weight > max_weight_capacity:
            print("\n[!] ERROR: FLIGHT ABORTED!")
            print("Ship is overweight! (", total_weight, "/", max_weight_capacity, kg, ")")
            print("Going back to main menu. Please use Option 6 to reduce weight.")
            # Because we DON'T use 'break' here, the main loop just restarts and sends them to the menu!
            
        # Liftoff
        else:
            print("\n[SUCCESS] PRE-FLIGHT CHECKS PASSED!")
            print("Total Weight:", total_weight, "/", max_weight_capacity, kg)
            
            # We calculate the final profits exactly when we need them
            total_profit = (titanium_weight * titanium_price) + (platinum_weight * platinum_price) + (alien_artifact_weight * alien_artifacts_price)
            
            print("Expected Profit: $" + str(total_profit))
            print("Engines ignited. Taking off! You win!")
            
            # Step 4: Game Over
            break



    if a == 6:
        print("--- WHICH CARGO TO REDUCE? ---")
        print("1) Titanium (", titanium_weight, kg, ")")
        print("2) Platinum (", platinum_weight, kg, ")")
        print("3) Alien Artifacts (", alien_artifact_weight, kg, ")")
        print("4) Cancel")

    
        while True:
            j = input(': ')
            try:
                j = int(j)
                break
            except:
                print("Enter the valid option only")
                continue
                
        if j == 1:
            while True:
                k = input("Please Enter the weight \n:")
                try:
                    k = int(k)
                    if k <= titanium_weight:
                        titanium_weight = titanium_weight - k  
                        print("Removed", k, kg, ". New Titanium weight:", titanium_weight, kg)
                        break
                    else:
                        print("You can't remove more than you have!")
                except ValueError:
                    print("Number Only")
                    
            
    

        if j == 2:
            while True:
                m = input("Please Enter the weight \n:")
                try:
                    m = int(m)
                    if m <= platinum_weight:
                        break
                    else:
                        print("You can't remove more than you have!")
                except ValueError:
                    print("Numbers Only, Understood")
                    continue
            platinum_weight = platinum_weight - m
            platinum_cost = platinum_weight * platinum_price
            print("New Platinum weight is:", platinum_weight, kg)
            
        

        if j == 3:
            print("Current Artifacts loaded:", alien_artifact_weight, kg)
            while True:
                o = input("Please Enter the weight \n:")
                try:
                    o = int(o)
                    if o <= alien_artifact_weight:
                        break
                    else:
                        print("You can't remove more than you have!")
                except ValueError:
                    print("Numbers only")
                    continue
            alien_artifact_weight = alien_artifact_weight - o
            alien_artifact_cost = alien_artifact_weight * alien_artifacts_price
            print("Removed", o, kg, ". New Artifact weight:", alien_artifact_weight, kg)



        if j == 4:  
            print("Returning to main menu....")
        
        




if total_weight > max_weight_capasity:
    print("Flight has be aborted. \nOverload, please reduce the weight")
elif total_weight == max_weight_capasity:
    print("Flight has be aborted. \n100% weight capacity has been occupied \nPleasse ruduce the weight")
elif total_weight < max_weight_capasity:
    print("The carried weighr witin limit, Proceed to fly")
else:
    print("Flight has been aborted due to unknown disterbance")


                

  



        
        







       

        



