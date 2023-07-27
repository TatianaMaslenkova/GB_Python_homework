"""
Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. Определите какие вещи влезут в
рюкзак передав его максимальную грузоподъёмность. Достаточно вернуть один допустимый вариант.
*Верните все возможные варианты комплектации рюкзака.
"""

data = {"Палатка": 5, "Котелок": 0.5, "Топор": 2, "Шашлык": 4, "Спички": 0.1, "Вода": 3, "Орехи": 1,
        "Спальник": 2.5, "Удочка": 1.1, "Надувная лодка": 3.8}
print(f"Список вещей с их весами: {data}")

backpack_capacity = float(input("Введите максимальную грузоподъёмность рюкзака (в кг): "))

items_to_take = []
all_items_weight = 0
for k, v in data.items():
    all_items_weight += v
if all_items_weight > backpack_capacity:
    capacity = backpack_capacity
    available_weight = 0
    for k, v in data.items():
        if v <= capacity:
            capacity -= v
            available_weight += v
            items_to_take.append(k)
    items_not_taken = []
    for el in data:
        if el not in items_to_take:
            items_not_taken.append(el)
    print(f"Общий вес рюкзака: {available_weight:.1f}. Поместилось: {items_to_take}. Не поместилось: {items_not_taken}")
else:
    print(f"Вместимость рюкзака ({backpack_capacity}) позволила взять все вещи: {data}.")
