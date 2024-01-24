# Password Strength Checker
import re
print("check your passwords strength\n","Enter your password - ")
passwrd = input()
if len(passwrd)<=8:
    print("password must contain minimum 8 characters")

elif not re.search("[A-Z]",passwrd):
    print("password must contain Capital letter")
elif not re.search("[a-z]", passwrd):
    print("password must contain small letter")
elif not re.search("[0-9]", passwrd):
    print("password must contain integers")
else:
    print("password is valid and strong")
