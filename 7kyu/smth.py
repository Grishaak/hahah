def tower_builder(n_floors):
    tower_list = []
    string = "*"
    for i in range(n_floors):
        tower_list.append(" " * (n_floors - 1) + string + (n_floors - 1) * " ")
        print(string)
        n_floors -= 1
        string += "**"
    return tower_list

def tower_builder(n):
    return [("*" * (i*2-1)).center(n*2-1) for i in range(1, n+1)]

my_list = tower_builder(6)
print(my_list)
#
# text = "*"
# text = " "*2 + text + " " *3
# print(list(text))
