import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules


def association_mining_func(dataset_path):
    # Load the dataset
    data = pd.read_csv(dataset_path, sep=";")

    # Drop non-numeric columns for association rule mining
    data_numeric = data.select_dtypes(include=["int", "float"])

    # Convert numeric columns to binary
    data_binary = data_numeric.apply(
        lambda x: pd.cut(x, bins=2, labels=["low", "high"])
    )

    # Convert binary columns to 0 and 1
    data_binary.replace({"low": 0, "high": 1}, inplace=True)

    # Perform frequent itemset mining
    frequent_itemsets = apriori(data_binary, min_support=0.1, use_colnames=True)

    # Generate association rules
    rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)

    return rules
