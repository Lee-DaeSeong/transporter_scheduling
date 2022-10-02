import random
import pandas as pd
import math


class block:
    def __init__(self, no, weight, start_node, end_node, start_time, end_time, start_pos, end_pos, dist):
        self.no = no
        self.weight = weight
        self.start_node = start_node
        self.end_node = end_node
        self.start_time = start_time
        self.end_time = end_time
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.dist = dist

    def __str__(self):
        ret = 'no: {}, weight: {}, start_node: {}, end_node: {}, time: {} ~ {}, pos: {} -> {}, dist: {}' \
            .format(self.no, self.weight, self.start_node, self.end_node, self.start_time, self.end_time, self.start_pos, self.end_pos, self.dist)
        return ret


# file_name = './data/map.xlsx'
file_name = r'C:\Users\dleot\PycharmProjects\transporter_scheduling\create_data\data\map.xlsx'
df = pd.read_excel(file_name, engine='openpyxl')
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

    start_node = random.randint(1, 30)
    end_node = random.randint(1, 30)
    while start_node == end_node:
        end_node = random.randint(1, 30)

    start_time = 9
    if random.random() <= 0.7:
        start_time = random.randint(9, 13)
    end_time = random.randint(9, 18)

    while start_time + 4 >= end_time:
        end_time = random.randint(9, 18)

    start_pos = [df.iloc[start_node]['x'], df.iloc[start_node]['y']]
    end_pos = [df.iloc[end_node]['x'], df.iloc[end_node]['y']]
    dist = math.dist(start_pos, end_pos) / 1000
    blocks.append(block(i, w, start_node, end_node, start_time, end_time, start_pos, end_pos, dist))

# for block in blocks:
#     print(block)
# blocks.sort(key = lambda x:x.end_time)
