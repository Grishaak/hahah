def row_sum_odd_numbers(n):
    count = 0
    sum = 0
    index = 0
    while n > 0:
        count += n
        n -= 1
    count = (count*2)
    for i in range(count):
        if i % 2 != 0:
            sum += i
            index += 1
    return sum, index


number = 5

print(row_sum_odd_numbers(number))
