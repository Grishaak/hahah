def narcissistic(value):
    size = len(str(value))
    new_list = [int(i) for i in str(value)]
    total = 0
    for i in new_list:
        total += int(i) ** size
    if total == value:
        return True
    return False


val = 154
flag = narcissistic(val)
print(flag)
