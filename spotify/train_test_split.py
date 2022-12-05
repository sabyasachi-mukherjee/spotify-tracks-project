import pandas as pd


class DatasetSplit:
    """This is for the train-test split."""

    @classmethod
    def return_train(cls, dataframe: pd.DataFrame) -> pd.DataFrame:
        length_training_set = int(0.8 * len(dataframe))
        train_set = dataframe.iloc[:length_training_set]
        return train_set

    @classmethod
    def return_test(cls, dataframe: pd.DataFrame) -> pd.DataFrame:
        length_training_set = int(0.8 * len(dataframe))
        test_set = dataframe.iloc[length_training_set:]
        return test_set
