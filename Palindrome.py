import math
input_string=input("Enter string to check:")
palindrome=True
for i in range(math.floor(len(input_string)/2)):
    if input_string[i] != input_string[(len(input_string)-1)-i]:
        palindrome = False
if palindrome:
    print("Its a palindrome string")
else:
    print("Its not a palindrome string")