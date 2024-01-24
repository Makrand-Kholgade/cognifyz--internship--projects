# Palindrome Checker
while(True):
    def Palindrome(string1):
        return string1[::-1]
    print("Please give the string")
    string1 = str(input())
    if string1==Palindrome(string1):
        print("Given String is Palindrome")
    else:
        print("Given String is Not a Palindrome")
    continue