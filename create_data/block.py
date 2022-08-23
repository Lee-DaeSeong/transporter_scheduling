import random
import pandas as pd
import math


class block:
    def __init__(self, no, weight, start_node, end_node, start_time, end_time, dist):
        self.no = no
        self.weight = weight
        self.start_node = start_node
        self.end_node = end_node
        self.start_time = start_time
        self.end_time = end_time
        self.dist = dist

    def __str__(self):
        ret = 'no: {}, weight: {}, start_node: {}, end_node: {}, time: {} ~ {}. dist: {}'\
            .format(self.no, self.weight, self.start_node, self.end_node, self.start_time, self.end_time, self.dist)
        return ret


blocks = []
for i in range(1, 101):
    w = random.random()
    if w <= 0.07:
        w = random.randint(1, 50)
    elif w <= 0.18:
        w = random.randint(50, 150)
    elif w <= 0.29:
        w = random.randint(150, 250)
    elif w <= 0.47:
        w = random.randint(250, 350)
    elif w <= 0.66:
        w = random.randint(350, 450)
    elif w <= 0.81:
        w = random.randint(450, 500)
    elif w <= 0.92:
        w = random.randint(500, 600)
    elif w <= 1:
        w = random.randint(600, 700)

    x = random.randint(1, 30)
    y = random.randint(1, 30)
    while x == y:
        y = random.randint(1, 30)

    s = random.randint(9, 15)
    e = random.randint(9, 18)

    while s + 2 >= e:
        e = random.randint(9, 18)

    df = pd.read_excel('map.xlsx', engine='openpyxl')
    maps = list(zip(df['x'], df['y']))
    dist = math.dist(maps[x], maps[y])
    blocks.append(block(i, w, x, y, s, e, dist))

