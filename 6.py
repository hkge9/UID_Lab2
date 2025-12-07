def diff_lists(list1, list2):
    result = []
    for i in range(len(list1)):
        result.append(list1[i] - list2[i])
    return result


a = [5, 4, 3]
b = [2, 1, 3]


c = diff_lists(a, b)

print("Исходный список 1:", a)
print("Исходный список 2:", b)
print("Разница списков:", c)
