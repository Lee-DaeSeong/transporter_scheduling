import pandas as pd
import numpy as np
import csv
import pathlib
from block import blocks
file_name = 'transporter.csv'
file = pathlib.Path(file_name)

if file.exists():
    pass
else:
    file.touch()