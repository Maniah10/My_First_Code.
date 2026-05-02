total = 0
a = input("Enter the Number: ")
a = float(a)
while True:
    while True:
        op = input("Enter the Operation Sign: ")
        if op == "+" or op == "-" or op == "*" or op == "/":
            break
        else:
            print("Enter Valide Oprator Sign: ")
    b = input("Enter the Number: ")
    b = float(b)

    if op == "+":
        total = a + b
        print(a + b)
    if op == "-":
        total = a - b
        print(a - b)
    if op == "*":
        total = a * b
        print(a * b)
    if op == "/":
        total= a / b
        print(a / b)
 #Now aks the user to whether they want ot continue or not?
    question = input("Continue? y/n ").lower()
    if question == "n":
        break
    else:
        a = total



    