
cook_book = {}
a = []
with open('recipes.txt', 'r', encoding='utf-8') as f:
    for dish in f:
        for ingredient in range(int(f.readline()) + 1):
            norm_str = f.readline().strip().split(' | ')
            if len(norm_str) == 3:
                items = {'ingredient_name': norm_str[0], 'quantity': norm_str[1], 'measure': norm_str[2]}
                a.append(items)
        cook_book[dish.strip()] = a
        a = []


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ing in cook_book[dish]:
            shop_list.update({ing['ingredient_name']: {'measure': ing['measure'],
                                                       'quantity': int(ing['quantity']
                                                                       ) * person_count * dishes.count(dish)}})
    return shop_list




