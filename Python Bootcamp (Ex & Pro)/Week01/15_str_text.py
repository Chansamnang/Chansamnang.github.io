arr = []
i = 0
while True:
    text = input("Enter a text: ")
    if text != 'Generate':
        arr.append(text)
    elif text == 'Generate':
        for i in arr:
            print("<p>"+i+"</p>")
        break