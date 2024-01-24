# Temperature Conversion
x = "Fahrenheit"
y = "Celsius"
print("Temperature conversion Program\n","Give the conversion value with unit")
print("1 - Fahrenheit to Celsius, 2 - Celsius to Fahrenheit")
try:
    U1 = int(input())
except Exception as e2:
    print("Wrong Input, Please Try Again")
    exit()
if U1<1 or U1>2:
    print("Wrong input please try again")
    exit()
else:
    pass
if U1==1:
    n = x
else:
    n = y
print("Enter the Value in", n)
try:
    temp1 = int(input())
except Exception as e2:
    print("Wrong Input, Please Try Again")
    exit()
if n == x:
    print("Value in Celsius is\n", "-", ((temp1-32)*(5/9)))
else:
    print("Value in Fafhrenheit is\n", "-", ((temp1 * 9/5)+(32)))