num = input("Enter a number : ")
if not num.isdigit():
    print(num + " is not a valid number")
elif int(num) % 2 == 0:
    print(num + " is EVEN")
else:
    print(num + " is ODD")