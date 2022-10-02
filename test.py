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
                    pick_up_time = random.uniform(max(trans.works_time[-1][1], block.start_time), 18 + 1)

                prev_to_start_dist = math.dist(prev, block.start_pos) / 1000
                start_to_end_dist = math.dist(block.start_pos, block.end_pos) / 1000

                prev_to_start_time = prev_to_start_dist / trans.empty_speed
                start_to_end_time = start_to_end_dist / trans.work_speed
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


population = generate_population(100)

for t in population[0]:
    print(t.works_time)


def get_fitness(pop):
    score = 0
    transporter_cnt = 0
    using_time = 0
    for t in pop:
        if t.works:
            transporter_cnt += 1
            for start, end in t.works_time:
                using_time += end - start

    # return transporter_cnt, using_time
    return transporter_cnt


def select_survivors(population, best_sample, lucky_few):
    fitness = [[x, get_fitness(x)] for x in population]
    fitness.sort(key=lambda x: x[1])

    next_generation = []
    for i in range(best_sample):
        next_generation.append(fitness[i][0])

    for lucky in random.sample(fitness, k=lucky_few):
        next_generation.append(lucky)

    random.shuffle(next_generation)
    return next_generation


# survivors = select_survivors(population, 30, 20)

