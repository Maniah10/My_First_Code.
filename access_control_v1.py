# Set the password
a = 753951
a = int(a)
# Giving 3 attempts
attempt = 4

# Asking for the password and converting it into int
password = input("Pleasse Enter the Password \n: ")
while True:
    try:
        password = int(password)
        break
    except:
        password = input("Please enter numeric password only \n:")
        continue

    while password != a:
        attempt = attempt - 1
        print("Access Denied")
        print("You have",attempt,"attempts left")
        password = input("Pleasse Enter the Right Password \n:")

        # If 0 attempts remain the code will exit
        if attempt == 0 :
            break

    # If the password is correct you will get the access 
    if int(password) == a:
        print("Access Granted")
        

    
    
        

    


    


   








    
    


    


    


    



    
        







