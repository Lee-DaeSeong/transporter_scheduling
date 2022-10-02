import pandas as pd
import numpy as np
import csv
import pathlib

file_name = r'C:\Users\dleot\PycharmProjects\transporter_scheduling\create_data\data\transporter.csv'
file = pathlib.Path(file_name)


class transporter:
    def __init__(self, no, avaialbe_weight, empty_speed, work_speed):
        self.no = no
        self.avaialbe_weight = avaialbe_weight
        self.empty_speed = empty_speed
        self.work_speed = work_speed
        self.works = []
        self.works_time = []
    def __str__(self):
        ret = 'no: {}, avaiable_weight: {}, empty_speed: {}, work_speed: {}, works: {}, works_time: {}'.format(self.no, self.avaialbe_weight,
                                                                                    self.empty_speed, self.work_speed, self.works, self.works_time)
        return ret


if file.exists():
    df = pd.read_csv(file)
    temp = list(zip(df['no'] - 1, df['avaiable_weight'], df['empty_speed'], df['work_speed']))
    transporters = []
    for n, a, e, w in temp:
        transporters.append(transporter(n, a, e, w))

    for transporter in transporters:
        print(transporter)
else:
    #file.touch()
    print(0)