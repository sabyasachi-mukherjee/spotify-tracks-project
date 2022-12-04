# Initialise main.py
import pandas as pd


class DataTransformations:
    @classmethod
    def preprocess(cls, df: pd.DataFrame) -> pd.DataFrame:
        "This function transforms our dataframes"
        df["release_date"] = df["release_date"].astype("datetime64[ns]")
        df["key"] = df["key"].astype("category")
        df["time_signature"] = df["time_signature"].astype("category")
        df["mode"] = df["mode"].astype("category")
        df["explicit"] = df["explicit"].astype("category")
        df["popularity"] = (
            df["popularity"] >= 64
        )  # 90th percentile of popularity for tracks released in and after 2012
        df["popularity"] = df["popularity"].astype(int)
        return df.query("release_date>= 2012").query("key != -1").drop_duplicates()
