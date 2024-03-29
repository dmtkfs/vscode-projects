import pandas as pd
import numpy as np
from mlxtend.frequent_patterns import apriori


def frequent_mining_func(dataset_path, min_support=0.1):

    def preprocess_data(df):

        # Replace missing values in numeric columns with their median values
        numeric_cols = df.select_dtypes(include=np.number).columns
        df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())

        # Remove columns that are not numeric to run Apriori
        non_numeric_cols = df.select_dtypes(exclude=np.number).columns
        df = df.drop(columns=non_numeric_cols)

        # Convert numeric columns to binary based on their median
        for col in numeric_cols:
            median_value = df[col].median()
            df[col] = (df[col] > median_value).astype(int)

        return df

    # Load the dataset from the appropriate file, using ; as separator
    df = pd.read_csv(dataset_path, sep=";")

    # Pre-processing to make data suitable for frequent pattern mining
    df_preprocessed = preprocess_data(df)

    # Use Apriori to find frequent itemsets, given a min support threshold
    frequent_itemsets = apriori(
        df_preprocessed,
        min_support=min_support,
        use_colnames=True,
    )

    # Convert the frozenset objects to strings to improve readability
    frequent_itemsets["itemsets"] = frequent_itemsets["itemsets"].apply(
        lambda x: ", ".join(map(str, x))
    )

    return frequent_itemsets
