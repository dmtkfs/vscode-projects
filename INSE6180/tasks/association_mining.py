import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules


def association_mining_func(dataset_path):
    # Load the dataset with semicolon (;) as the delimiter
    data = pd.read_csv(dataset_path, sep=";")

    # Select only numeric columns for association rule mining, as required by the Apriori algorithm
    data_numeric = data.select_dtypes(include=["int", "float"])

    # Convert numeric values to binary categories (low and high) based on the median
    # We transform the data into a suitable format for binary association rule mining
    data_binary = data_numeric.apply(
        lambda x: pd.cut(x, bins=2, labels=["low", "high"])
    )

    # Set pandas option to prevent silent downcasting in future versions, ensuring data integrity
    pd.set_option("future.no_silent_downcasting", True)

    # Replace the categorical labels ('low', 'high') with integers (0, 1) for the Apriori algorithm
    data_binary = data_binary.replace({"low": 0, "high": 1}).astype(int)

    # Perform Apriori to identify frequent itemsets with a minimum support of 0.2
    # 'use_colnames' allows the use of original column names instead of column indices
    frequent_itemsets = apriori(data_binary, min_support=0.2, use_colnames=True)

    # Generate association rules using the 'lift' metric, with a min threshold to drop less interesting rules
    rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)

    # Convert the frozensets to strings for readability.
    rules["antecedents"] = rules["antecedents"].apply(lambda x: ", ".join(x))
    rules["consequents"] = rules["consequents"].apply(lambda x: ", ".join(x))

    return rules
