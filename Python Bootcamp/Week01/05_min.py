num1 = input("Enter a first number: ")
num2 = input("Enter a second number: ")
if int(num1) < int(num2):
    print(num1 + " < " + num2)
elif int(num2) < int(num1):
    print(num2 + " < " + num1)
else:
    print(num1 + " = " + num2)