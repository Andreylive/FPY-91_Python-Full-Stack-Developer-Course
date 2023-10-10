def open_cookbook():
    """Create a cookbook from a file"""
    with open('recipes.txt', 'r', encoding='utf-8') as f:
        cook_book: dict = {} # save all dish info and their ingredients
        lines = f.read().split('\n\n') # separate text for certain dishes
        for dish in lines:
            ingredients_list: list = [] # save all ingredients for one dish
            dish_info = dish.split('\n') # separate dish info, for name, number of ingredients and ingredient info
            dish_name, ingredient_number = dish_info[0], int(dish_info[1])
            ingredients = dish_info[2: 2+ingredient_number]
            for ingredient in ingredients:
                ingredient_name, quantity, measure = ingredient.split(' | ')
                ingredient_dict = {
                    'ingredient_name': ingredient_name,
                    'quantity': quantity,
                    'measure': measure
                }
                ingredients_list.append(ingredient_dict)
            cook_book[dish_name] = ingredients_list
    return cook_book

cook_book = open_cookbook()
print(cook_book)


