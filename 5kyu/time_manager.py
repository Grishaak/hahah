def format_duration(seconds):
    if not seconds:
        return "now"
    year = seconds // 3600 // 24 // 365
    days = ((seconds // 3600) // 24) % 365
    hours = (seconds // 3600) % 24
    minutes = (seconds // 60) % 60
    seconds = seconds % 60
    date_dictionary = {"year": year, "day": days, "hour": hours, "minute": minutes, "second": seconds}
    my_list = []
    for key, value in date_dictionary.items():
        if value:
            my_list.append((f"{str(value)} {key}s" if value > 1 else f"{str(value)} {key}"))
    string = ""
    for i in range(len(my_list)):
        if len(my_list) == 1:
            return my_list[i]
        if (i + 1) == len(my_list) - 1:
            string += f"{my_list[i]} and {my_list[i + 1]}"
            return string
        else:
            string += f"{my_list[i]}, "


print(format_duration(0))
