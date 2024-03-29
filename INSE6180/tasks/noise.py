import pandas as pd
import numpy as np
from mlxtend.frequent_patterns import apriori


def frequent_pattern_mining_with_noise(dataset_path, min_support=0.1, noise_level=0.1):

    # Load the dataset and prepare it for mining by one-hot encoding categorical variables
    df = pd.read_csv(dataset_path, sep=";")
    df_encoded = pd.get_dummies(df, drop_first=True)
    numeric_columns = df_encoded.select_dtypes(include=["number"]).columns
    df_numeric = df_encoded[numeric_columns]

    # Add noise to the dataset focusing on sensitive columns if specified
    noise_data = add_targeted_noise(df_numeric, noise_level)

    # Use Apriori to mine frequent itemsets from the dataset with added noise
    noise_itemsets = apriori(
        noise_data.astype(bool), min_support=min_support, use_colnames=True
    )

    # Convert frozensets to strings for readability.
    noise_itemsets["itemsets"] = noise_itemsets["itemsets"].apply(
        lambda x: ", ".join(map(str, x))
    )

    return noise_itemsets


def add_targeted_noise(df, noise_level=0.1, sensitive_columns=[]):

    noise_data = df.copy()
    # Iterate through each sensitive column to apply noise directly
    for col in sensitive_columns:
        if col in df.columns:
            num_rows = len(df)
            num_noise_rows = int(num_rows * noise_level)
            noise_indices = np.random.choice(df.index, num_noise_rows, replace=False)
            noise_values = np.random.choice([0, 1], size=(num_noise_rows,))
            noise_data.loc[noise_indices, col] = noise_values

    return noise_data
