def positive():
    print("Положительное")

def negative():
    print("Отрицательное")

def test():
    n = int(input("Введите число: "))
    if n > 0:
        positive()
    elif n < 0:
        negative()
    else:
        print("Ноль")


test()
