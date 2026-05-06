import time
current_hour = int(time.strftime('%H'))
a =  current_hour
a = float(a)
if a >= 00.01 and a <= 12.00 :
    print("Good Morning Dear, Have A good Day")
elif a >=12.01 and a <= 16.00 :
    print('Good Afternoon')
elif a >= 16.01 and a <= 20.00 :
    print('Good Evening')
elif a >= 20.01 and a <= 24.00 :
    print('Good Night Sweet Dreams')
elif  a == 00.00:
   print('Good Night Sweet Dreams')

    


