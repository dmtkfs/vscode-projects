import pandas as pd
import numpy as np
from mlxtend.frequent_patterns import apriori


def frequent_pattern_mining_with_noise(dataset_path, min_support=0.1, noise_level=0.1):
    """
    Perform frequent pattern mining with noise addition on the dataset.

    Parameters:
        dataset_path (str): Path to the CSV file containing the dataset.
        min_support (float): Minimum support threshold for frequent pattern mining.
        noise_level (float): The percentage of noise transactions to add.

    Returns:
        DataFrame: The frequent patterns mined from the dataset with noise.
    """
    # Load the dataset
    df = pd.read_csv(dataset_path, sep=";")

    # Preprocess the dataset by encoding categorical variables and dropping non-numeric columns
    df_encoded = pd.get_dummies(df, drop_first=True)
    numeric_columns = df_encoded.select_dtypes(include=["number"]).columns
    df_numeric = df_encoded[numeric_columns]

    # Add noise to the dataset
    noise_data = add_targeted_noise(df_numeric, noise_level)

    # Perform frequent pattern mining
    noise_itemsets = apriori(
        noise_data.astype(bool), min_support=min_support, use_colnames=True
    )

    # Convert frozensets to strings
    noise_itemsets["itemsets"] = noise_itemsets["itemsets"].apply(
        lambda x: ", ".join(map(str, x))
    )

    return noise_itemsets


def add_targeted_noise(df, noise_level=0.1, sensitive_columns=[]):
    """
    Add noise to sensitive itemsets in the dataset selectively.

    Parameters:
        df (DataFrame): Original dataset.
        noise_level (float): The percentage of noise transactions to add to sensitive itemsets.
        sensitive_columns (list): Columns considered sensitive.

    Returns:
        DataFrame: Dataset with added noise to sensitive itemsets.
    """
    noise_data = df.copy()
    for col in sensitive_columns:
        if col in df.columns:
            num_rows = len(df)
            num_noise_rows = int(num_rows * noise_level)
            noise_indices = np.random.choice(df.index, num_noise_rows, replace=False)
            noise_values = np.random.choice([0, 1], size=(num_noise_rows,))
            noise_data.loc[noise_indices, col] = noise_values

    return noise_data
