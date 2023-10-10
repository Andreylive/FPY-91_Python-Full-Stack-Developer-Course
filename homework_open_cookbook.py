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
# print(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    """Clacalute set of ingredients for ceratiin amount of people"""
    cook_book = open_cookbook()
    ingredient_summary = {}
    for dish in dishes:
        ingredients = cook_book[dish]
        for ingredient in ingredients:
            if ingredient['ingredient_name'] in ingredient_summary:
                ingredient_summary[ingredient['ingredient_name']]['quantity'] += (int(ingredient['quantity']) * person_count)
            else:
                ingredient_dict = {
                    'measure': ingredient['measure'],
                    'quantity': int(ingredient['quantity']) * person_count
                    }
                ingredient_summary[ingredient['ingredient_name']] = ingredient_dict
    return ingredient_summary

ingredients = get_shop_list_by_dishes(['Омлет', 'Омлет'], 2)
print(ingredients)



