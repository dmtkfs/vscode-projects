import pandas as pd
from tasks.association_mining import association_mining_func
from tasks.fuzzy import fuzzy_mining_func
from tasks.frequent_mining import frequent_mining_func
from tasks.noise import frequent_pattern_mining_with_noise
import warnings


def main():

    # Suppress DeprecationWarning
    warnings.filterwarnings("ignore", category=DeprecationWarning)

    # dataset paths
    dataset_path = r"database\student-mat.csv"
    fuzzy_dataset_path = r"outputs\association_rules.csv"

    # execute association rule mining
    rules = association_mining_func(dataset_path)

    # save association rules results table
    rules.to_csv("outputs/association_rules.csv", index=True)

    # execute fuzzy mining
    fuzzy_data = fuzzy_mining_func(fuzzy_dataset_path)

    # save the fuzzy mining results table
    fuzzy_data.to_csv("outputs/hidden_association_rules.csv", index=True)

    # execute frequent pattern mining
    frequent_itemsets = frequent_mining_func(dataset_path)

    # save the frequent pattern mining results table
    frequent_itemsets.to_csv("outputs/frequent_itemsets.csv", index=True)

    # execute frequent pattern mining with noise
    frequent_patterns_with_noise = frequent_pattern_mining_with_noise(
        dataset_path, min_support=0.1, noise_level=0.1
    )

    print(frequent_patterns_with_noise)

    # save the noise mining results table
    frequent_patterns_with_noise.to_csv("outputs/noise_itemsets.csv", index=True)


main()
