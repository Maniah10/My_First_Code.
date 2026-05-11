a = 753951
a = int(a)
attempt = 3
while attempt > 0:
    password = input("Please Enter the Password \n:")
    try:
        password = int(password)
    except:
        print("Please Enter Numeric Password Only ")
        continue
    if password == a:
        print("Access Granted")
        break
    else:
        print("Access Denied")
        attempt = attempt - 1
        print("You Have",attempt,"attempts left")
        continue

    



