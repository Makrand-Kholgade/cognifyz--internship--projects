# Calculator Program

while (True):
    print("\tCALCULATOR")
    print("First number")
    try:
        inp1 = int(input())
    except Exception as e1:
        print("Wrong Input please try again")
        exit()
    print("Select the Operator(+,-,*,/)")
    str1 = str(input())
    try:
        print("Second number")
        inp2 = int(input())
    except Exception as e3:
        print("Wrong Input please try again")
        continue
    if str1 == "+":
        print("Your Ansewer is")
        print(inp1 + inp2)
    elif str1 == "-":
        print("Your Ansewer is")
        print(inp1 - inp2)
    elif str1 == "*":
        print("Your Ansewer is")
        print(inp1 * inp2)
    elif str1 == "/":
        print("Your Ansewer is")
        print(inp1 / inp2)
    else:
        print("Wrong input check again")
    