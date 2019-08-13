def fun(*list):
    unique = []
    for x in list:
        if x not in unique:
            unique.append(x)
    unique.sort()
    print(unique)
fun(4,2,19,50,49,48,1,2,3,4,5)