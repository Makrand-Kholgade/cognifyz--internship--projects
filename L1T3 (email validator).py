# Email Validator
while True:
    email = input("Enter your email : ")
    k,j,d=0,0,0

    if (len(email)>=6):
        if email[0].isalpha():
            if ("@" in email) and (email.count("@")==1):
                if (email[-4]==".") ^ (email[-3]=="."):
                    for i in email:
                        if i==i.isspace():
                            k=1
                        elif i.isalpha():
                            if i==i.upper():
                                j=1
                        elif i.isdigit():
                            continue
                        elif i=="_" or i=="." or i=="@":
                            continue
                        else:
                            d=1

                    if k==1 or j==1 or d==1:
                        print("Invalid Email")
                    else:
                        print("Valid Email")
                else:
                    print("Invalid email")
            else:
                print("Invalid Email")
        else:
            print("Invalid Email")
    else:
        print("Invalid Email")

    continue















# import re
#
# list_of_symb = [[A,Z], [a-z], ]
# print("Email Validator")
# print("Type your Email")
# em = str(input())
#
# def validate(email):
#     if(re.search(list_of_symb, email)):
#         print("This is the valid Email")
#     else:
#         print("this is the Invalid Email")
# if __name__ == '__main__':
#     email = em
#     validate(email)