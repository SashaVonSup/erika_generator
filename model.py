# -*- coding: utf-8 -*-

import pickle
from random import randint
from bisect import bisect_left


spaces = ' \n\t\v'
dots = '.!?'
START = '\\1'
END = '\\0'


class Model:
    words: dict = {}

    def add_pair(self, first: str, second: str):
        if not first or not second:
            return
        words1 = self.words.get(first, {})
        words1[second] = words1.get(second, 0) + 1
        self.words[first] = words1

    def fit(self, filename: str):
        with open(filename) as file:
            text = file.read()
        prev = START
        cur = ''
        for c in text:
            if c in spaces:
                self.add_pair(prev, cur)
                if cur:
                    prev, cur = cur, ''
            elif c in dots:
                if cur:
                    self.add_pair(prev, cur)
                    self.add_pair(cur, END)
                else:
                    self.add_pair(prev, END)
                prev, cur = START, ''
            elif c.isalpha():
                cur += c.lower()
        self.add_pair(prev, cur)
        self.add_pair(cur if cur else prev, END)

    def save(self, filename: str):
        with open(filename, 'wb') as file:
            pickle.dump(self.words, file)

    def load(self, filename: str):
        with open(filename, 'rb') as file:
            self.words = pickle.load(file)

    def generate(self, start: str):
        word = start if start in self.words.keys() else START
        while word != END:
            cur = self.words[word]
            words = list(cur.keys())
            weights = [0] * len(words)
            for i in range(len(words)):
                weights[i] = weights[i-1] + cur[words[i]]
            x = randint(0, weights[-1])
            word = words[bisect_left(weights, x)]
            yield word
