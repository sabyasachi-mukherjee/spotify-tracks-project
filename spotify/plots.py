import pandas as pd
import matplotlib.pyplot as plt

class SpotifyPlots:
    @classmethod
    def distribution_plot(cls, dataframe: pd.DataFrame, column_name = "popularity"):
        ax = plt.gca()
        dataframe[column_name].plot(kind = 'hist', ax = ax, title = f"Distribution of {column_name} in tracks after 2012.")
        plt.legend(loc = "best")
        plt.show()

