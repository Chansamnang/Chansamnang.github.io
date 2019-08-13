def fun(*list):
    unique = []
    new = []
    for x in list:
        if not x.isnumeric():
            unique.append(x)
    for x in sorted(set(unique)):
        new.append(x)
    print(new)

fun('abc', '4', '3', '2', 'dza', 'def', 'def')
