import tensorflow as tf
import numpy as np
import pandas as pd

data = pd.read_csv('ThoraricSurgery3.csv')
data = data.dropna()

x데이터 = data.iloc[:, 0:15].value.tolist()
y데이터 = data.iloc[:, 15].value.tolist()

