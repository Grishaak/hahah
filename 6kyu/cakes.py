def cakes(recipe, available):
    result_cake = min(
        [available[i] // recipe[i] if i in recipe and (recipe[i] <= available[i]) else 0 for i in recipe])
    return result_cake


recipe_cake = {"sugar": 130, "eggs": 10, "flour": 200}
available_cake = {"flour": 1000, "sugar": 1000, "eggs": 6, "milk": 2000}

print(cakes(recipe_cake, available_cake))
