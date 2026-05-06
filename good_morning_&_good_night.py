while True:
# Asking user for the input
    a = input("please Insert The Current Time  \nOnly 24.00 hr formate is accepted  \n: ")
    a = float(a)       # Converting the input into float
    
    if a >= 00.01 and a <= 12.00 :
        print("Good Morning Dear, Have A good Day")
    elif a >=12.01 and a <= 16.00 :
        print('Good Afternoon')
    elif a >= 16.01 and a <= 20.00 :
        print('Good Evening')
    elif a >= 20.01 and a <= 24.00 :
        print('Good Night Sweet Dreams')
    elif a == 00.00 :
        print('Good Night Sweet Dreams')
    else: print('Invalid time')
        