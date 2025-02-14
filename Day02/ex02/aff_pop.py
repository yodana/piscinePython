""" Program who contains function to plot a graph """

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
from load_csv import load

def add_suffix(value, pos):
    if value >= 1000000:
        return f"{value / 1000000:1.0f}M"
    elif value >= 1000:
        return f"{value / 1000:1.0f}k"
    else:
        return str(int(value))


def convert(numbers: str) -> float:
    """ def convert(numbers: str)  -> float:
        Function who convert K or M to real numbers """
    if 'M' in numbers:
        return int(float(numbers.replace('M', '')) * 1000000)
    elif 'K' in numbers:
        return int(float(numbers.replace('K', '')) * 1000)


def aff_pop(name: str):
    """ def aff_pop(name, csv)
        Function who plot a graph according to the name"""
    try:
        csv = load("population_total.csv")
        f_df = csv.loc[:, 'country':'2050']
        values1 = f_df.loc[f_df['country'] == name].iloc[0, 1:]
        years = values1.index.astype(int)
        values1 = [convert(v) for v in values1.values]
        values2 = f_df.loc[f_df['country'] == 'France'].iloc[0, 1:]
        values2 = [convert(v) for v in values2.values]
    except Exception as e:
        print("The name is not valid ", e)
    try:
        fig, ax = plt.subplots()
        plt.plot(years, values1, label=name)
        ax.yaxis.set_major_formatter(add_suffix)
        ax.yaxis.set_major_locator(ticker.MaxNLocator(nbins=4))
        ax.xaxis.set_major_locator(ticker.MaxNLocator(nbins=7))
        plt.plot(years, values2, color='green', label="France")
        plt.title("Population Projections")
        plt.xlabel("Year")
        plt.ylabel("Population")
        plt.legend(loc=4)
        plt.show()
    except Exception as e:
        print("An error happened", e)
