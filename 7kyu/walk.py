def is_valid_walk(walk):
    flag = False
    if len(walk) > 10 or len(walk) < 10:
        return flag
    count_w = 0
    count_e = 0
    count_s = 0
    count_n = 0
    for i in walk:
        if i == "w":
            count_w += 1
            if count_e > 1:
                count_e = count_e - count_w
        if i == "e":
            count_e += 1
            if count_w > 1:
                count_w = count_w - count_e
        if i == "s":
            count_s += 1
            # if count_n > 1:
            #     count_n = count_n - count_s
        if i == "n":
            count_n += 1
            # if count_s > 1:
            #     count_s = count_s - count_n
    if count_n == count_s == count_w == count_e:
        flag = True
    return flag


list = ['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's']

sum = is_valid_walk(list)
print(sum)
