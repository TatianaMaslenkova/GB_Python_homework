"""
Решите квадратное уравнение 5x**2-10x-400=0 последовательно сохраняя переменные a, b, c, d, x1 и x2
Попробуйте решить уравнения с другими значениями a, b, c
(Квадратное уравнение имеет вид: ax² + bx + c = 0, решать через дискриминант: D = b2 − 4ac
если D < 0, корней нет; если D = 0, есть один корень; если D > 0, есть два различных корня
"""
a = float(input('Решим квадратное уравнение. Введите a: '))
b = float(input('Введите b: '))
c = float(input('Введите c: '))

if a == 0 and b == 0 and c == 0:
    print('Корней бесконечное множество')
elif a == 0 and b == 0:
    print('Корней нет')
else:
    if a == 0:
        x = - c / b
        print(f"Один корень x = {round(x, 2)}")

    if b == 0 and c == 0:
        print('Это уравнение имеет один корень x = 0')

    if a != 0 and b == 0 and c != 0:
        if ((- c) / a) < 0:
            print('Корней нет')
        elif ((-c) / a) > 0:
            solution = abs(c / a) ** 0.5
            x1 = solution
            x2 = -solution
            print(f"Два корня: x1 = {round(x1, 2)}, x2 = {round(x2, 2)}")

    if a != 0 and b != 0 and c == 0:
        print(f"Два корня: x1 = 0, x2 = {(round((-b / a), 2))}")

    if a > 1:
        b = b / a
        c = c / a
        a = a / a

    if a != 0 and b != 0 and c != 0:
        d = ((b ** 2) - (4 * a * c))
        if d < 0:
            print('Корней нет')
        elif d == 0:
            sol = -b / 2 * a
            print(f"Один корень: x = {(round(sol, 2))}")
        else:
            x1 = (-b + d ** 0.5) / (2 * a)
            x2 = (-b - d ** 0.5) / (2 * a)
            case1 = min(x1, x2)
            case2 = max(x1, x2)

            if case1 != case2:
                print(f"Два корня: x1 = {(round(case1, 2))}, x2 = {(round(case2, 2))}")
            else:
                print(f"Один корень: x = {(round(case1, 2))}")
