def fib(n: int):
    fib_list = [0, 1]
    if not n:
        return 0
    for i in range(1, n):
        fib_list.append(fib_list[i - 1] + fib_list[i])
    return fib_list[-1]


print(fib(2000000))
