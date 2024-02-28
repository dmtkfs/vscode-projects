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

    pd.set_option("future.no_silent_downcasting", True)
    # Convert binary columns to 0 and 1
    # Assuming data_binary is a categorical Series
    data_binary = data_binary.replace({"low": 0, "high": 1}).astype(int)

    # Perform frequent itemset mining
    frequent_itemsets = apriori(data_binary, min_support=0.2, use_colnames=True)

    # Generate association rules
    rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)

    # Convert frozenset to string
    rules["antecedents"] = rules["antecedents"].apply(lambda x: ", ".join(x))
    rules["consequents"] = rules["consequents"].apply(lambda x: ", ".join(x))

    return rules
