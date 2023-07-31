"""
Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции. Дополнительно сохраняйте все операции
поступления и снятия средств в список. (Задача 6 семинара 2: Напишите программу банкомат. ✔ Начальная сумма равна нулю
✔ Допустимые действия: пополнить, снять, выйти ✔ Сумма пополнения и снятия кратны 50 у.е. ✔ Процент за снятие — 1.5% от суммы
снятия, но не менее 30 и не более 600 у.е. ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
✔ Нельзя снять больше, чем на счёте ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией,
даже ошибочной ✔ Любое действие выводит сумму денег - Разбейте её на отдельные операции — функции.
- Дополнительно сохраняйте все операции поступления и снятия средств в список.
"""

from datetime import datetime

balance = 0
withdrawal_fee_rate = 0.015
min_withdrawal_fee = 30
max_withdrawal_fee = 600
count = 0
count_lim_fee = 0.03
wealth_sum_lim = 5000000
wealth_tax = 0.1
log_operations = []


def check_divisibility():
    while True:
        cash = int(input('Введите сумму кратную 50: '))
        if cash % 50 == 0:
            return cash
        else:
            print('Введенная сумма не кратна 50!')


def add_cash(amount):
    global balance
    global count
    balance += amount
    count += 1
    print(f'Внесены наличные в сумме: {amount}')


def withdraw_cash(amount):
    global balance
    global count
    balance -= amount
    count += 1
    withdrawal_fee_amount = amount * withdrawal_fee_rate
    if withdrawal_fee_amount < min_withdrawal_fee:
        withdrawal_fee_amount = min_withdrawal_fee
    elif withdrawal_fee_amount > max_withdrawal_fee:
        withdrawal_fee_amount = max_withdrawal_fee
    balance -= withdrawal_fee_amount
    print(f'Списаны проценты за снятие в сумме: {withdrawal_fee_amount}')


def add_percent():
    global balance
    count_lim_amount = count_lim_fee * balance
    print(f'Начислены проценты в размере: {count_lim_amount:.2f}')
    balance = balance + count_lim_fee * balance


while True:
    operation = input('Введите желаемую операцию:\nw - снять наличные\na - внести наличные\n'
                      'h - показать историю операций\nq - выйти:\n').lower()
    if balance > wealth_sum_lim:
        wealth_tax_amount = balance * wealth_tax
        balance -= wealth_tax_amount
        log_operations.append([str(datetime.now()), "Удержан налог на богатсво", -wealth_tax_amount])
        print(f'Удержан налог на богатство в размере: {wealth_tax_amount}')
    if operation == 'w':
        cash = check_divisibility()
        if cash < balance:
            withdraw_cash(cash)
            log_operations.append([str(datetime.now()), "Снятие наличных", -cash])
        else:
            print('На счете недостаточно средств!\n')
    elif operation == 'a':
        cash = check_divisibility()
        add_cash(cash)
        log_operations.append([str(datetime.now()), "Внесение наличных", cash])
    elif operation == 'h':
        print('История операций:\n')
        print(log_operations)
    elif operation == 'q':
        print('Выход из банкомата')
        exit()
    else:
        print('Нет такой операции. Пожалуйста, повторите ввод!')

    if count % 3 == 0:
        add_percent()

    print(f'Текущий баланс = {balance:.2f}')
