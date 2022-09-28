list1 = [1, 2, 3, 4]
list2 = [3, 8, 3, 4]
list3 = [3, 8, 3, 4]

def add_num(a, b, c):
    return (a + b) * c

x = map(add_num, list1, list2, list3)
print(list(x))