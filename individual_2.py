#!/usr/bin/env python3
# -*- config: utf-8 -*-

import pandas as pd
import numpy as np

# Использовать объект Series, содержащий следующие индексы: название пункта назначения
# рейса; номер рейса; тип самолета. Написать программу, выполняющую следующие
# действия: ввод с клавиатуры данных в DataFrame, с заданными колонками; вывод на экран
# пунктов назначения и номеров рейсов, обслуживаемых самолетом, тип которого введен с
# клавиатуры; если таких рейсов нет, выдать на дисплей соответствующее сообщение.


def add(iter_dat):
    temp_1 = input('Введите пункт назначения> ')
    temp_2 = input('Введите номер рейса> ')
    temp_3 = input('Введите тип самолета> ')
    dat_frame.loc[iter_dat] = [temp_1, temp_2, temp_3]


def find():
    temp_f = input('Какого типа самолет> ')
    print(f'\nВот такие рейсы мы нашли\n{dat_frame[dat_frame["Тип самолета"] == temp_f]}')


if __name__ == '__main__':
    first_ser = pd.Series(['STV', '1234', 'IL-72'],
                          ['Пункт назначения', 'Номер рейса', 'Тип самолета'])
    iter_dat = 1
    dat_frame = pd.DataFrame(
        {
            'Пункт назначения': {iter_dat: first_ser['Пункт назначения']},
            'Номер рейса': {iter_dat: first_ser['Номер рейса']},
            'Тип самолета': {iter_dat: first_ser['Тип самолета']},
        }
    )
    while True:
        comm = input('Введите команду> ')
        if comm == 'add':
            iter_dat += 1
            add(iter_dat)
        elif comm == 'find':
            find()
        elif comm == 'help':
            print('Помо4ник\nВвести новый рейс - add\n'
                  'Найти рейсы по самолету - find\n'
                  'Покать таблицу - show\nПомо4ник - help'
                  'Выход - exit')
        elif comm == 'show':
            print(dat_frame)
        elif comm == 'exit':
            break
        else:
            print('Ошибка')
