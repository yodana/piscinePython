from load_csv import load
import matplotlib.pyplot as plt


def add_suffix(value, pos):
    if value >= 1000000:
        return f"{value / 1000000:1.0f}M"
    elif value >= 1000:
        return f"{value / 1000:1.0f}k"
    else:
        return str(int(value))


def projection():
    """ def projection()
        Function who plot a graph"""
    try:
        c_i = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
        csv_life = load("life_expectancy_years.csv")
        l_df = csv_life.loc[:, ['country', '1900']]
        i_df = c_i.loc[:, ['country', '1900']]
    except Exception as e:
        print("An error happened", e)
    try:
        fig, ax = plt.subplots()
        plt.scatter(i_df['1900'], l_df['1900'], c="C0")
        plt.xscale("log")
        plt.xticks([300, 1000, 10000])
        ax.xaxis.set_major_formatter(add_suffix)
        plt.title("1900")
        plt.xlabel("Life Expectancy")
        plt.ylabel("Gross domectic product")
        plt.show()
    except Exception as e:
        print("An error happened", e)
