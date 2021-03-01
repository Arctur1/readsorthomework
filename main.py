
cookbook = {}


def parse_dish(n):
    for i in range(int(n)):
        ingredient = {}
        s = f.readline().strip('\n').split(" | ")
        ingredient['ingredient_name'] = s[0]
        ingredient['quantity'] = s[1]
        ingredient['measure'] = s[2]
        cookbook[name].append(ingredient)


with open('recipes.txt', encoding='utf-8') as f:

        while True:
            name = f.readline().strip('\n')
            cookbook[name] = []
            n = f.readline().strip('\n')
            parse_dish(n)
            if f.readline() == "":
                break




def get_shop_list_by_dishes(dishes, person_count):
    ingredients = {}
    for dish in dishes:
        for ingredient in cookbook[dish]:
            if ingredient['ingredient_name'] in ingredients:
                ingredients[ingredient['ingredient_name']]['quantity']\
                    = str(int(ingredients[ingredient['ingredient_name']]['quantity']) + int(ingredient['quantity'])* person_count)
            else:
                ingredients[ingredient['ingredient_name']] \
                = {'quantity' : str(int(ingredient['quantity']) * person_count), 'measure' : ingredient['measure']}
    return ingredients

print(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2))

with open("1.txt", encoding='utf-8') as f1, open("2.txt", encoding='utf-8') as f2, open("3.txt", encoding='utf-8') as f3:
    file_1 = f1.readlines()
    file_2 = f2.readlines()
    file_3 = f3.readlines()
    files_unsorted = {"1.txt": file_1, "2.txt": file_2, "3.txt": file_3}
    files_sorted = sorted(files_unsorted, key=lambda key: len(files_unsorted[key]))
    print(files_sorted)

with open('result.txt', 'w', encoding='utf-8') as f:
    for item in files_sorted:
        f.write(f"{item}\n{len(files_unsorted[item])}\n {''.join(files_unsorted[item])}\n")



