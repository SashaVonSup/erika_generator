# -*- coding: utf-8 -*-

from sys import argv
from model import Model


if __name__ == '__main__':
    if len(argv) < 3:
        print('Наименьшее возможное количество аргументов - 2: название файла модели и названия файлов корпуса')
        exit(1)
    model = Model()
    for arg in argv[2:]:
        model.fit(arg)
    model.save(argv[1])
