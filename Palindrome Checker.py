var = input(("Enter a value: "))
if(var == var[::-10]):
    print("The input is a palindrome")
else:
    print("The input is not a palindrome")