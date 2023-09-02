import logging
import argparse
from datetime import datetime

"""
Возьмите любые 1-3 задания из прошлых домашних заданий. Добавьте к ним логирование ошибок и полезной информации.
Также реализуйте возможность запуска из командной строки с передачей параметров.
Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции. Дополнительно сохраняйте все
операции поступления и снятия средств в список. (Задача 6 семинара 2: Напишите программу банкомат. ✔ Начальная сумма
равна нулю ✔ Допустимые действия: пополнить, снять, выйти ✔ Сумма пополнения и снятия кратны 50 у.е. ✔ Процент за
снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е. ✔ После каждой третей операции пополнения или снятия
начисляются проценты - 3% ✔ Нельзя снять больше, чем на счёте ✔ При превышении суммы в 5 млн, вычитать налог на
богатство 10% перед каждой операцией, даже ошибочной ✔ Любое действие выводит сумму денег - Разбейте её на отдельные
операции — функции.
"""

logging.basicConfig(filename='Log/log_3.log',
                    filemode='a',
                    encoding='utf-8',
                    format='{levelname:<6} - {asctime} в строке {lineno:>3d} функция "{funcName}()" : {msg}',
                    style='{',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

balance = 0
withdrawal_fee_rate = 0.015
min_withdrawal_fee = 30
max_withdrawal_fee = 600
count = 0
count_lim_fee = 0.03
wealth_sum_lim = 5000000
wealth_tax = 0.1
log_operations = []


def check_divisibility(cash):
    if cash % 50 == 0:
        return cash
    else:
        res = 'Введенная сумма не кратна 50!'
        print(res)
        logger.warning(f'{str(datetime.now())} Введённая сумма: {cash}. Результат: {res}')


def add_cash(amount):
    global balance
    global count
    balance += amount
    count += 1
    res = f'Внесены наличные в сумме: {amount}'
    print(res)
    logger.info(f'{str(datetime.now())} Операция: внесение наличных в сумме: {res}')


def withdraw_cash(amount):
    global balance
    global count
    balance -= amount
    res = f'Операция: снятие наличных в сумме: {amount}'
    print(res)
    logger.info(f'{str(datetime.now())} Операция: снятие наличных в сумме: {amount}')
    count += 1
    withdrawal_fee_amount = amount * withdrawal_fee_rate
    if withdrawal_fee_amount < min_withdrawal_fee:
        withdrawal_fee_amount = min_withdrawal_fee
    elif withdrawal_fee_amount > max_withdrawal_fee:
        withdrawal_fee_amount = max_withdrawal_fee
    balance -= withdrawal_fee_amount
    res = f'Списаны проценты за снятие в сумме: {withdrawal_fee_amount}'
    print(res)
    logger.info(f'{str(datetime.now())} Операция: списание процентов за снятие наличных. Результат: {res}')


def add_percent():
    global balance
    count_lim_amount = count_lim_fee * balance
    res = f'Начислены проценты в размере: {count_lim_amount:.2f}'
    print(res)
    logger.info(f'{str(datetime.now())} Операция: начисление процентов. Результат: {res}')
    balance = balance + count_lim_fee * balance


if __name__ == '__main__':
    # parser = argparse.ArgumentParser(description='ATM')
    # parser.add_argument('-operation', type=int, action='append', help='1 - withdraw, 2 - add, 3 - quit')
    # parser.add_argument('-amount', type=int, action='append')
    # args = parser.parse_args()
    # вводим в терминал в формате $ python homework15_task3.py -operation 2 -amount 1000 -operation 2 -amount 5000000
    # -operation 1 -amount 100000 -operation 1 -amount 10035 -operation 3
    # for i in range(len(args.operation)):
    #     if balance > wealth_sum_lim:
    #         wealth_tax_amount = balance * wealth_tax
    #         balance -= wealth_tax_amount
    #         res = f'Удержан налог на богатство в размере: {wealth_tax_amount}'
    #         print(res)
    #         logger.info(f'{str(datetime.now())} Операция: удержание налога на богатство. Результат: {res}')
    #     if args.operation[i] == 1:
    #         for j in range(len(args.amount)):
    #             if i == j:
    #                 checked_sum = check_divisibility(args.amount[j])
    #                 if args.amount[j] < balance and checked_sum:
    #                     withdraw_cash(args.amount[j])
    #                 elif not checked_sum:
    #                     print('Сумма должна быть кратна 50!')
    #                 else:
    #                     res = 'На счете недостаточно средств!'
    #                     print(res)
    #                     logger.error(f'{str(datetime.now())} Операция: снятие наличных. Ошибка! {res}')
    #     elif args.operation[i] == 2:
    #         for j in range(len(args.amount)):
    #             if i == j:
    #                 checked_sum = check_divisibility(args.amount[j])
    #                 add_cash(checked_sum)
    #     elif args.operation[i] == 3:
    #         print('Выход из банкомата')
    #         logger.info(f'{str(datetime.now())} Операция: выход из банкомата')
    #         exit()
    #     else:
    #         res = 'Нет такой операции. Пожалуйста, повторите ввод!'
    #         print(res)
    #         logger.error(f'{str(datetime.now())} Ошибка! {res}')
    #
    #     if count % 3 == 0:
    #         add_percent()
    #
    #     curr_balance = f'Текущий баланс = {balance:.2f}'
    #     print(curr_balance)
    #     logger.info(f'{str(datetime.now())} {curr_balance}')

    while True:
        operation = input('Введите желаемую операцию:\nw - снять наличные\na - внести наличные\n'
                          'q - выйти:\n').lower()
        if balance > wealth_sum_lim:
            wealth_tax_amount = balance * wealth_tax
            balance -= wealth_tax_amount
            res = f'Удержан налог на богатство в размере: {wealth_tax_amount}'
            print(res)
            logger.info(f'{str(datetime.now())} Операция: удержание налога на богатство. Результат: {res}')
        if operation == 'w':
            cash = int(input('Введите сумму кратную 50: '))
            checked_cash = check_divisibility(cash)
            if cash < balance and checked_cash:
                withdraw_cash(checked_cash)
            elif not checked_cash:
                print('Сумма должна быть кратна 50!')
            else:
                res = 'На счете недостаточно средств!'
                print(res)
                logger.error(f'{str(datetime.now())} Операция: снятие наличных. Ошибка! {res}')
        elif operation == 'a':
            cash = int(input('Введите сумму кратную 50: '))
            checked_cash = check_divisibility(cash)
            add_cash(checked_cash)
        elif operation == 'q':
            print('Выход из банкомата')
            logger.info(f'{str(datetime.now())} Операция: выход из банкомата')
            exit()
        else:
            res = 'Нет такой операции. Пожалуйста, повторите ввод!'
            print(res)
            logger.error(f'{str(datetime.now())} Ошибка! {res}')

        if count % 3 == 0:
            add_percent()

        curr_balance = f'Текущий баланс = {balance:.2f}'
        print(curr_balance)
        logger.info(f'{str(datetime.now())} {curr_balance}')
