def fun(*list):
    unique =[x for x in list if x.isnumeric()>0]
    temp = []
    new = []
    for x in unique:
        if int(x) > 0 :
            temp.append(x)
    for x in sorted(set(temp)):
        new.append(x)
    print(new)
fun('abc','4','4','4','4','2','3','-2','dza','def')