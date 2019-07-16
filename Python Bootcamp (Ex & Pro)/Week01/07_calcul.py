def l(n):
    k = input("Enter a number: ")
    try:
        n += int(k)
        print("Total" +n)
        l(n)
    except :
        if k == 'exit':
            exit()
        print(n)
        l(n)
l(0)