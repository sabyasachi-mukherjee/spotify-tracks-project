import pandas as pd
import matplotlib.pyplot as plt

class SpotifyPlots:
    @classmethod
    def distribution_plot(cls, dataframe: pd.DataFrame, column_name = "popularity"):
        ax = plt.gca()
        (dataframe[column_name]
        .plot(kind = 'hist', ax = ax, title = f"Distribution of {column_name} in tracks after 2012.")
        )
        plt.legend(loc = "best")
        plt.show()
    @classmethod
    def attribute_vs_popularity(cls, dataframe: pd.DataFrame, column_name = "danceability"):
        dataframe_new = dataframe.copy()
        dataframe_new['qcut']  = pd.qcut(dataframe_new[column_name], q = 5, duplicates= 'drop')
        ax = plt.gca()
        (dataframe_new.groupby('qcut')
        .agg(average_popularity = ('popularity','mean'))
        .reset_index()
        .plot(x = "qcut", y = "average_popularity", ax = ax)
        )
        plt.legend(loc = "best")
        plt.xlabel(f"quantile_{column_name}")
        plt.xticks(rotation=90)
        plt.show()
    

        
    


