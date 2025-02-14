""" Program who contains function to plot a graph """

import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load

def aff_life(name: str):
    """ def aff_life(name)
        Function who plot a graph of population according to the name country"""
    try:
        csv = load("life_expectancy_years.csv")
        values = csv.loc[csv['country'] == name].iloc[0, 1:]
    except Exception:
        print("The name is not valid")
    try:
        plt.plot(values.index.astype(int), values.values)
        plt.title(name + " Life expectancy Projections")
        plt.xlabel("Year")
        plt.ylabel("Life expectancy")
        plt.show()
    except Exception:
        print("An error happened")
