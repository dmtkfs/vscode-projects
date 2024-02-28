import pandas as pd
from tasks.association_mining import association_mining_func
from tasks.fuzzy import fuzzy_mining_func


def main():

    # Define the path to your dataset
    dataset_path = r"database\student-mat.csv"
    fuzzy_dataset_path = r"outputs\association_rules.csv"

    # Perform association rule mining
    rules = association_mining_func(dataset_path)

    # Save the association rules to a CSV file
    rules.to_csv("outputs/association_rules.csv", index=True)

    threshold = 0.5
    alpha1 = 0.5  # Weight for IS
    alpha2 = 0.5  # Weight for DOC

    # Perform fuzzy mining
    fuzzy_data = fuzzy_mining_func(fuzzy_dataset_path, alpha1, alpha2)

    # Save the modified dataset with hidden association rules
    fuzzy_data.to_csv("outputs/hidden_association_rules.csv", index=False)
    print(fuzzy_data.head())


main()
