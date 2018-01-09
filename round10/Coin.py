# Intro to programming
# Classes and Objects
# Phan Viet Anh
# 256296

import random


class Coin:

    def __init__(self):

        self.sideUp = 'Heads'

    def toss(self):
        if random.randint(0, 1) == 0:
            self.sideUp = 'Heads'
        else:
            self.sideUp = 'Tails'

    def get_sideup(self):
        return self.sideUp


def main():
        coin = Coin()
        a = coin.get_sideup()
        print(a)
        for index in range(0,10):
            coin.toss()
            print(index, coin.get_sideup(), sep=' > ')
main()
