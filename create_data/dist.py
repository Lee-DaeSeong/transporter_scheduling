import pandas as pd

file_name = 'map.xlsx'
df = pd.read_excel(file_name, engine='openpyxl')
maps = list(zip(df['x'], df['y']))
for i in range(len(maps)):
    print(maps[i])