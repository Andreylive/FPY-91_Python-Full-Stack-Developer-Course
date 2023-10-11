cook_book_dict: dict = {}

def add_dish():
    print('Если вы хотите добавить блюдо в кулинарну книгу, напишите наименование и количество ингредиентов')
    dish_name = input('Введите имя блюда\n')
    ingredients_number = int(input('Укажите количество ингредиентов в блюде\n'))
    ingredient_list = []
    for i in range(ingredients_number):
        print(f"Чтобы добавить в кулинарную книгу блюдо '{dish_name}' необходимо добавить все ингредиенты, их количества и еденицы измерения")
        ingredient_dict = {}
        ingredient_name = input('Введите имя ингредиента: \n')
        ingredient_dict['ingredient_name'] = ingredient_name
        quantity = int(input('Введите количество ингредиента (без единиц измерения): \n'))
        ingredient_dict['quantity'] = quantity
        measure = input('Введите единицу измерения сокращенно (шт., мл., л., кг.) \n')
        ingredient_dict['ingredient_measure'] = measure
        ingredient_list.append(ingredient_dict)
    cook_book_dict[dish_name] = ingredient_list    
    return cook_book_dict

add_dish()

print(cook_book_dict)