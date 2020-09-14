# -*- coding: utf-8 -*-

from sys import argv
from model import Model, START


if __name__ == '__main__':
    if len(argv) < 2:
        print('Наименьшее возможное количество аргументов - 1: название файла модели')
        exit(1)
    model = Model()
    model.load(argv[1])
    start = argv[-1].lower() if len(argv) >= 3 else START
    res = []
    while len(res) < 2:
        res = [i for i in model.generate(start)]
    res = argv[2:] + res[:-1]

    print(*res)
