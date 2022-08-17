import math
from random import random
from time import time

def getRandomName():
    n = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "r", "s", "t", "v", "w", "x", "y", "z"]
    t = ["a", "e", "i", "o", "u"]
    r = getRandomInt(5, 7, True)
    o = ""
    i = True
    while len(o) < r:
        if i:
            o += str(n[getRandomInt(0, len(n) - 1)])
            i = False
        else:
            o += str(t[getRandomInt(0, len(t) - 1)])
            i = True
    a = 10 - r
    tiempo = str(time()).split('.')
    #return o + str(getRandomInt(math.pow(10, a - 1), math.pow(10, a)))
    return F"{o}{tiempo[0]}{tiempo[1][:3]}"


def getRandomInt(n, t, r=False):
    o = 1 if r else 0
    return int(math.floor(random() * (t - n + o)) + n)

