def count_div3(a, b):
    count = 0
    for num in range(a, b + 1):
        if num % 3 == 0:
            count += 1
    return count

def count_div4(a, b):
    count = 0
    for num in range(a, b + 1):
        if num % 4 == 0:
            count += 1
    return count

def count_div5(a, b):
    count = 0
    for num in range(a, b + 1):
        if num % 5 == 0:
            count += 1
    return count


a = int(input("Введите начало отрезка: "))
b = int(input("Введите конец отрезка: "))

print("Чисел, делящихся на 3:", count_div3(a, b))
print("Чисел, делящихся на 4:", count_div4(a, b))
print("Чисел, делящихся на 5:", count_div5(a, b))
