import pandas as pd
import numpy as np
from mlxtend.frequent_patterns import apriori
from sklearn.preprocessing import LabelEncoder


def frequent_mining_func(dataset_path, min_support=0.1):
    """
    Performs frequent pattern mining on the dataset.

    Args:
    - dataset_path (str): Path to the CSV file containing the dataset.
    - min_support (float): Minimum support threshold for frequent itemsets.

    Returns:
    - frequent_itemsets (pandas DataFrame): DataFrame of frequent itemsets.
    """

    def preprocess_data(df):
        """
        Preprocesses the DataFrame for frequent pattern mining.

        Args:
        - df (pandas DataFrame): DataFrame to preprocess.

        Returns:
        - df_preprocessed (pandas DataFrame): Preprocessed DataFrame suitable for frequent pattern mining.
        """
        # Fill missing values in numeric columns with the median
        numeric_cols = df.select_dtypes(include=np.number).columns
        df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())

        # Drop non-numeric columns
        non_numeric_cols = df.select_dtypes(exclude=np.number).columns
        df = df.drop(columns=non_numeric_cols)

        # Convert numeric columns to binary
        for col in numeric_cols:
            median_value = df[col].median()
            df[col] = (df[col] > median_value).astype(int)

        return df

    # Read CSV file into a pandas DataFrame
    df = pd.read_csv(dataset_path, sep=";")

    # Preprocess the data
    df_preprocessed = preprocess_data(df)
    # Perform frequent pattern mining using Apriori algorithm
    frequent_itemsets = apriori(
        df_preprocessed,
        min_support=min_support,
        use_colnames=True,
    )

    # Convert frozensets to strings
    frequent_itemsets["itemsets"] = frequent_itemsets["itemsets"].apply(
        lambda x: ", ".join(map(str, x))
    )

    return frequent_itemsets
