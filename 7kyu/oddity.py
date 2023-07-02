def odd(num):
    total = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total


number = int(input("Введите лимит последовательности натуральных чисел: "))
summary = odd(number)
print(summary)
