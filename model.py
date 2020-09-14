# -*- coding: utf-8 -*-

import pickle
from random import randint
from bisect import bisect_left


class Model:
    words: dict = {}
    spaces = ' \n\t\v'

    def add_pair(self, first: str, second: str):
        if not first or not second:
            return
        words1 = self.words.get(first, {})
        words1[second] = words1.get(second, 0) + 1
        self.words[first] = words1

    def fit(self, filename: str):
        with open(filename) as file:
            text = file.read()
        prev = '\1'  # '\1' вместо начала текста
        cur = ''
        for c in text:
            if c in self.spaces:
                self.add_pair(prev, cur)
                prev, cur = cur, ''
            elif c.isalpha():
                cur += c.lower()
        self.add_pair(prev, cur)
        self.add_pair(cur, '\0')  # '\0' вместо конца текста

    def save(self, filename: str):
        with open(filename, 'wb') as file:
            pickle.dump(self.words, file)

    def load(self, filename: str):
        with open(filename, 'rb') as file:
            self.words = pickle.load(file)

    def generate(self, start: str):
        word = start
        while word != '\0':
            cur = self.words[word]
            words = cur.keys()
            weights = [0] * len(words)
            for i in range(len(words)):
                weights[i] = weights[i-1] + cur[words[i]]
            x = randint(0, weights[-1])
            cur = bisect_left(weights, x)
            yield cur
