number = 1234


# z = number % 60
# y = (number // 60) % 60
# x = number // 3600
# print(x)
# print(y)
# print(z)
# result = f"{('0' + str(x)) if (int(x) < 10) else str(x)}" \
#          f":{('0' + str(y)) if (int(y) < 10) else str(y)}" \
#          f":{('0' + str(z)) if (int(z) < 10) else str(z)}"
# print(result)


# def make_readable(integer_seconds):
#     if integer_seconds >= 359999:
#         return "99:59:59"
#     seconds = integer_seconds % 60
#     minuts = (integer_seconds // 60) % 60
#     hours = integer_seconds // 3600
#     return f"{('0' + str(hours)) if int(hours) < 10 else str(hours)}" \
#            f":{('0' + str(minuts) if int(minuts) < 10 else str(minuts))}" \
#            f":{('0' + str(seconds)) if int(seconds) < 10 else str(seconds)}"


# def make_readable(integer_seconds):
#     if integer_seconds >= 359999: return "99:59:59"
#     return f"{('0' + str(integer_seconds // 3600)) if int(integer_seconds // 3600) < 10 else str(integer_seconds // 3600)}" \
#            f":{('0' + str((integer_seconds // 60) % 60) if int((integer_seconds // 60) % 60) < 10 else str((integer_seconds // 60) % 60))}" \
#            f":{('0' + str(integer_seconds % 60)) if int(integer_seconds % 60) < 10 else str(integer_seconds % 60)}"


def make_readable(s):
    return '{:02}:{:02}:{:02}'.format(s // 3600, s // 60 % 60, s % 60)


print(make_readable(number))
