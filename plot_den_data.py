import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import random as rand
import time
import random_numbers as chaos
import os
from mpl_toolkits.mplot3d import Axes3D


def main():
    df = pd.read_csv('fractaldata.csv')
    if 'z' in df.columns:
        '''3d'''
        x, y, z = 0,0,0
        df = pd.read_csv('fractaldata.csv')
        fig = plt.figure()
        ax = fig.add_subplot(111,projection = '3d')
        scat = ax.scatter(df['x'], df['y'], df['z'],c = 'black')
        ax.axis([0, 1, 0, 1])
        plt.show()
    else:
        '''2d'''
        x, y= 0,0
        df = pd.read_csv('fractaldata.csv')
        fig, ax = plt.subplots()
        scat = ax.scatter(df['x'], df['y'], c = 'black')
        ax.axis([0, 1, 0, 1])
        plt.show()

if __name__ == '__main__':
    main()
