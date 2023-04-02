cook_book = {}

with open('recipes.txt', 'r', encoding='UTF-8') as file:
    while True:
        dish_name = file.readline().strip()
        if not dish_name:
            break

        cook_book[dish_name] = []

        ingredients_count = int(file.readline().strip())

        for i in range(ingredients_count):
            ingredient_data = file.readline().strip().split(' | ')
            ingredient_name = ingredient_data[0]
            quantity = int(ingredient_data[1])
            measure = ingredient_data[2]

            cook_book[dish_name].append({'ingredient_name': ingredient_name,
                                          'quantity': quantity,
                                          'measure': measure})

        file.readline()

print(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            name = ingredient['ingredient_name']
            measure = ingredient['measure']
            quantity = ingredient['quantity'] * person_count
            if name not in shop_list:
                shop_list[name] = {'measure': measure, 'quantity': quantity}
            else:
                shop_list[name]['quantity'] += quantity
    return shop_list


print(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2))
