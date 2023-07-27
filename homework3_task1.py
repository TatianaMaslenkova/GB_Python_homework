"""
✔ Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей.
Ответьте на вопросы: ✔ Какие вещи взяли все три друга ✔ Какие вещи уникальны, есть только у одного друга
✔ Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
✔ Для решения используйте операции с множествами. Код должен расширяться на любое большее количество друзей.
"""

data = {"Вася": ("Палатка", "Котелок", "Топор", "Спички", "Шашлык", "Орехи"),
        "Ваня": ("Палатка", "Котелок", "Топор"),
        "Петя": ("Палатка", "Котелок", "Топор", "Вода"),
        "Лёша": ("Палатка", "Котелок", "Орехи", "Вода", "Спирт")}

all_items_set = set()
for key in data:
    if not all_items_set:
        all_items_set = set(data[key])
    else:
        all_items_set = all_items_set.intersection(set(data[key]))
print(f"Все три друга взяли с собой:", *all_items_set)

friend_key = data.keys()
unique_items_set = set()
for friend in friend_key:
    to_be_removed = set(data[friend])
    unique_items_set = set(data[friend])
    all_except_one_set = set()
    for another_friend in friend_key:
        if another_friend != friend:
            unique_items_set = unique_items_set.difference(set(data[another_friend]))
            if not all_except_one_set:
                all_except_one_set = set(data[another_friend])
            else:
                all_except_one_set = all_except_one_set.intersection(set(data[another_friend]))
    all_except_one_set -= to_be_removed

    if unique_items_set:
        print(f"Уникальные вещи, которые есть только у {friend}:", *unique_items_set)
    if all_except_one_set:
        print(f"Вещи, которые есть у всех, кроме {friend}:", *all_except_one_set)
