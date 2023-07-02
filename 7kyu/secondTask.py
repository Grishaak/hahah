# return masked string

def descending_order_only_int(num):
    number = 0
    list = []
    count = 0
    i = 0
    while num >= 1:
        x = num % 10
        list.append(x)
        num //= 10
        count += 1
    list.sort(reverse=True)
    for i in range(len(list)):
        number += list[i] * 10**(count - i - 1)
    return number


def descending_order_by_string(num):
    num = str(num)
    num = int("".join(sorted(num, reverse=True)))
    return num


numberS = 99881122
print(descending_order_by_string(numberS))
print("\n")
print(descending_order_only_int(numberS))