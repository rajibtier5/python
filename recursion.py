i = 1


def myLoop():
    global i
    if i < 4:
        print("Hello Mitu!")
        i += 1
    else:
        return
    myLoop()


myLoop()
