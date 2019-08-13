def fun(*list):
    temp = []
    for x in list:
        temp.append(x)
    print(sorted(temp))
fun(4,2,19,50,49,48,1,2,3,4,5)