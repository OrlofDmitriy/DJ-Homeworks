from django.shortcuts import render

import copy

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }

def calculator(request, recipe):

    i = request.GET.get("servings", "")
    data = copy.deepcopy(DATA)
    if i:
        name_recipe = recipe
        ingredients = {}
        for ingredient, amount in data[name_recipe].items():
            ingredients[ingredient] = amount * int(i)
            data[name_recipe].update(ingredients)
        context = {
            "recipe": data[name_recipe]

        }
    else:
        name_recipe = recipe
        context = {
            "recipe": DATA[name_recipe]

        }

    return render(request, 'calculator/index.html', context)

