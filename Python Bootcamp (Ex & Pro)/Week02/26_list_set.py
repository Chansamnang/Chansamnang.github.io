def fun(*list):
    unique = []
    for x in list:
        if x not in unique:
            unique.append(x)
    for x in unique:
        print (x ,end=" ")
fun('456','123','789','123','abc','abc','def')