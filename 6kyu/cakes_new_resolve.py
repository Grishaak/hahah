# def cakes(recipe, available):
#     return min(available.get(i, 0))


recipe_cake = {"sugar": 200, "eggs": 1, "flour": 500}
available_cake = {"flour": 1500, "sugar": 500, "eggs": 5, "milk": 2042335140}

get_cake = min(available_cake.get(k, 0) // recipe_cake[k] for k in recipe_cake)
print(get_cake)
