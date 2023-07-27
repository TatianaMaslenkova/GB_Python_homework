"""
В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. Не учитывать знаки препинания и
регистр символов. За основу возьмите любую статью из википедии или из документации к языку.
"""

text = "Коллекция в Python — программный объект, хранящаий набор значений одного или различных типов, \
позволяющий обращаться к этим значениям, а также применять специальные функции и методы, зависящие от типа коллекции. Частая \
проблема при изучении коллекций заключается в том, что разобрав каждый тип довольно детально, обычно потом не уделяется \
достаточного внимания разъяснению картины в целом, не проводятся чёткие сходства и различия между типами, не показывается как \
одну и туже задачу решать для каждой из коллекций в сравнении. Вот именно эту проблему я хочу попытаться решить в данном цикле \
статей – рассмотреть ряд подходов к работе со стандартными коллекциями в Python в сравнении между коллекциями разных типов, а \
не по отдельности, как это обычно показывается в обучающих материалах. Кроме того, постараюсь затронуть некоторые моменты, \
вызывающие сложности и ошибки у начинающих. Для кого: для изучающих Python и уже имеющих начальное представление о коллекциях \
и работе с ними, желающих систематизировать и углубить свои знания, сложить их в целостную картину. Индексированность – каждый \
элемент коллекции имеет свой порядковый номер — индекс. Это позволяет обращаться к элементу по его порядковому индексу, \
проводить слайсинг («нарезку») — брать часть коллекции выбирая исходя из их индекса. Детально эти вопросы будут рассмотрены в \
дальнейшем в отдельной статье.Уникальность – каждый элемент коллекции может встречаться в ней только один раз. Это порождает \
требование неизменности используемых типов данных для каждого элемента, например, таким элементом не может быть список.\
Изменяемость коллекции — позволяет добавлять в коллекцию новых членов или удалять их после создания коллекции. \
(Отрывок взят с сайта Хабр)"

new_list = text.replace(".", " ").replace(",", "").replace("— ", "").replace("– ", "").replace("(", "") \
    .replace(")", "").lower().split()
# print(new_list)
words_frequency = {}
for word in new_list:
    words_frequency[word] = new_list.count(word)

sorted_frequency = dict(sorted(words_frequency.items(), key=lambda item: item[1], reverse=True))
# print(sorted_frequency)
count = 0
top_10 = {}
for word, n in sorted_frequency.items():
    if count < 10:
        top_10[word] = n
        count += 1
        continue
    else:
        break

print(f'ТОП-10 наиболеe часто встречающихся слов: {top_10}')
