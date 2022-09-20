import copy
import sys
import os
import math
from create_data.block import blocks
from create_data.transporter import transporters
import random


def generate_population(size):
    ret = []
    for _ in range(size):
        pop = copy.deepcopy(transporters)

        for block in blocks:
            hubo = []
            for t in pop:
                if t.avaialbe_weight >= block.weight:
                    hubo.append(t)

            while hubo:
                trans = hubo.pop(random.randint(0, len(hubo) - 1))
                if not trans.works:
                    prev = [0, 0]
                    pick_up_time = block.start_time
                else:
                    # 해당 트랜스포터의 맨 마지막 작업 뒤에 새로운 작업 추가
                    prev = [trans.works[-1].start_node, trans.works[-1].end_node]
                    pick_up_time = random.uniform(trans.works_time[-1][1], 18 + 1)

                prev_to_start = math.dist(prev, block.start_pos) / 1000
                start_to_end = math.dist(block.start_pos, block.end_pos) / 1000

                prev_to_start_time = prev_to_start / trans.empty_speed
                start_to_end_time = start_to_end / trans.work_speed
                finish_time = pick_up_time + prev_to_start_time + start_to_end_time

                flag = True
                for start, end in trans.works_time:
                    if not (pick_up_time >= end or finish_time <= start) or finish_time > 18:
                        flag = False
                        break

                if flag:
                    trans.works.append(block)
                    trans.works_time.append([pick_up_time, pick_up_time + prev_to_start_time + start_to_end_time])
                    break
        ret.append(pop)
    return ret


population = generate_population(10)


# for t in population[0]:
#     print(t.works_time)

def get_fitnees(pop):
    score = 0
    transporter_cnt = 0
    using_time = 0
    for t in pop:
        if t.works:
            transporter_cnt += 1
            for start, end in t.works_time:
                using_time += end - start

    return transporter_cnt, using_time

for pop in population:
    print(get_fitnees(pop))
