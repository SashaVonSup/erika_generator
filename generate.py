# -*- coding: utf-8 -*-

from sys import argv
from model import Model


if __name__ == '__main__':
    if len(argv) < 2:
        print('Наименьшее возможное количество аргументов - 1: название файла модели')
        exit(1)
    model = Model()
    model.load(argv[1])
    if len(argv) < 3:
        res = model.generate('\1')
    else:
        res = argv[2:] + list(model.generate(argv[-1].lower()))[:-1]
    print(*res)
