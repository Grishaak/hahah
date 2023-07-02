def digital_root(number):
    total = 0
    if number < 10:
        return number
    else:
        while number > 9:
            total += number % 10
            number //= 10
            if number < 10:
                total += number
                if total >= 10:
                    number = total
                    total = 0
    return total


number_1 = int(input())
summary = digital_root(number_1)
print(summary)
