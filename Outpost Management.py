# i am giving an option
rice = int(100)
dal = int(100)
vegitables = int(100)


soldir_details = {}



while True:
    a = input("---- OUTPOST MANAGEMENT---- \n(1)See supplies  \n(2)Add new supplies  \n(3)Add new soldirs/trainee  \n(4)See Soldir details \n(5)Current inventory longevity \n(6)Exit  \n: ")
    a = int(a)
             
    if a == 1:
        print(str('Rice: ') + str(rice) + str('kg'))
        print(str('Dal: ') + str(dal) + str('kg'))
        print(str('Vegitables: ') + str(vegitables) + str('kg'))                                 # first is done here




    if a == 2:
        c = []
        c = input("what do you like to add first: \n(1)rice  \n(2)dal  \n(3)vegitable \n: ")
        c = int(c)

        if c == 1 :
            r1 = input("rice: ")
            r1 = int(r1)
            rice = rice + r1
         

        if c == 2 :
            dd = input("dal: ")
            dd = int(dd)
            dal = dal + dd
       
        if c == 3 :
            v1 = input("vegitables: ")
            v1 = int(v1)
            vegitables = vegitables + v1
                               
# Successfully added new values




# Now for the 3rd option
    
    if a == 3:
        while True:
            soldir_id = input("Soldir ID:  ")
            if soldir_id.isdigit():
                break
            else:
                print("Invalid input! Please enter a valid ID number (numbers only).")
                      


            soldir_id = str(soldir_id) 
            

        soldir_name = input("Enter soldir name: ")
        soldir_name = str(soldir_name)

        soldir_details[soldir_id] = soldir_name
            

        print("Success! Total soldiers is now:", len(soldir_details))



# Solder details option 4
    if a == 4:
        print("----Soldire Details----")
        for l in soldir_details:
            print(l, ":", soldir_details[l])

        


# Now comes 5th option, how many days the current supply will last long
    if a == 5:
        r2 = ((rice * 2) / len(soldir_details))
        r2 = int(r2)
        r3 = r2 / 7
        r4 = str(round(r3)) + str(' Weeks')
        print(r4)

        
        d2 = ((dal * 2) / len(soldir_details)) 
        d2 = int(d2)
        d3 = d2 / 7
        d4 = str(round(d3)) + str(' Weeks')
        print(d4)


        v2 = ((vegitables * 2) / len(soldir_details))
        v2 = float(v2)
        v3 = v2 / 7
        v4 = str(round(v3)) + str(' Weeks')
        print(v4)


    if a == 6:
        print('have a good day :) ')  
        break











   





