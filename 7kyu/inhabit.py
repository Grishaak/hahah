def longest_consec(strarr, key):
    if (key > len(strarr)) or key <= 0 or len(strarr) <= 0:
        return ""
    list = []
    i = 0
    j = key
    while j <= len(strarr) + 1:
        kv = "".join(strarr[i:j])
        list.append(kv)
        i += 1
        j += 1
    maximum = max(list, key=len)
    return maximum


array = ["121", "FSSAA", "vxdafa", "A:!@dadsda", "PPPPPS"]

long = longest_consec(array, 2)
print(long)
