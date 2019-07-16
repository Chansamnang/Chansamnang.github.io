str = input("Enter a string : ")
newStr = ""
for i in range(0,len(str)):
    if str[i].islower():
        newStr += str[i].upper()
    elif str[i].isupper():
        newStr += str[i].lower()
    else:
        newStr += str[i]
print(newStr)