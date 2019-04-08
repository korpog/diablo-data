import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def scatter_plot(df):
    """ Show a scatter plot showing the relationship between leaderboard rank and paragon level """
    df.plot.scatter(x='Rank', y='Paragon', c='DarkBlue')
    plt.show()


def histogram(df):
    """ Show histograms of rift times (in milliseconds) and paragon levels  """
    df.hist(column=['Time', 'Paragon'], bins=20)
    plt.show()


def histogram_dates(df):
    """ Plot count of records for each week of the year """
    df.groupby(df['Completed on'].dt.weekofyear).count()['Completed on'].plot(
        kind="bar", legend=False, color='DarkBlue')
    plt.xlabel('Week of year')
    plt.ylabel('Count')
    plt.show()


def main():
    filename = 'us-dh-16.csv'
    df = pd.read_csv(filename, parse_dates=['Completed on'])
    print(df.corr())
    histogram_dates(df)


if __name__ == "__main__":
    main()
