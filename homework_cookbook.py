import os

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

ingredients = get_shop_list_by_dishes(['Омлет', 'Омлет', 'Запеченный картофель'], 2)
# print(ingredients)

def join_files():
    """Join text from several files into one file"""
    text_info = []

    with open('1.txt', 'r', encoding='utf-8') as f:
        file_name = '1.txt'
        lines =  f.readlines()
        lines_number = len(lines)
        lines = ''.join(lines)

    text_dict_1 = {
        'file_name': file_name,
        'lines_number': lines_number,
        'text': lines
        }
    
    text_info.append(text_dict_1)
 
    with open('2.txt', 'r', encoding='utf-8') as f:
        file_name = '2.txt'
        lines = f.readlines()
        lines_number = len(lines)
        lines = ''.join(lines)

        text_dict_2 = {
            'file_name': file_name,
            'lines_number': lines_number,
            'text': lines
        }
        
    text_info.append(text_dict_2)

    with open('3.txt', 'r', encoding='utf-8') as f:
        file_name = '3.txt'
        lines = f.readlines()
        lines_number = len(lines)
        lines = ''.join(lines)

    text_dict_3 = {
        'file_name': file_name,
        'lines_number': lines_number,
        'text': lines
        }
    
    text_info.append(text_dict_3)

    result_file = open("result_file.txt", "w", encoding='utf-8')

    with open('result_file.txt', 'a', encoding='utf-8') as f:
        for text_dict in text_info:
            text_dict = text_dict
            f.write(f" {text_dict['file_name']} \n")
            f.write(f" {text_dict['lines_number']} \n")
            f.write(f" {text_dict['text']} \n")
join_files()
