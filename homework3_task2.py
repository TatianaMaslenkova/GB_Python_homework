"""
Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов.
"""

init_lst = [5, 17, 17, 17, 25, 34, 34, True, True, None, False, "text", "text1", "text2", "text"]

new_list = []
for el in init_lst:
    if init_lst.count(el) > 1:
        new_list.append(el)
print(list(set(new_list)))
