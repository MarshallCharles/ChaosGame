import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import random as rand
import time
import random_numbers as chaos
import os

x, y= 0,0
df = pd.read_csv('fractaldata.csv')
fig, ax = plt.subplots()
scat = ax.scatter(df['x'], df['y'], c = 'black')

ax.axis([0, 1, 0, 1])
plt.show()
