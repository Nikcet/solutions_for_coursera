def back():
    a = int(input())
    if a != 0:
        back()
    return print(a)


back()
