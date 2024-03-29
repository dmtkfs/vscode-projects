import pandas as pd
import numpy as np


def fuzzy_mining_func(data_file_path, alpha1=0.5, alpha2=0.5):

    # Load the association rules dataset
    data = pd.read_csv(data_file_path)

    # Compute the count (Nj) for each antecedent
    Nj_dict = data["antecedents"].value_counts().to_dict()
    data["Nj"] = data["antecedents"].map(Nj_dict)

    # Calculate the Information Strength (IS) for each rule
    data["IS"] = (data["Nj"] * data["support"]) / data["antecedent support"]

    # Calculate the Degree Of Confidence (DOC) for each rule
    data["DOC"] = np.sqrt((data["confidence"] - data["consequent support"]) ** 2)

    # Compute the Best Information Value (BIV) for each rule by combining IS and DOC
    data["BIV"] = alpha1 * data["IS"] + alpha2 * data["DOC"]

    # Identify the rule with the minimum BIV, meaning the most sensitive
    best_row_index = data["BIV"].idxmin()

    # Prepare to hide the most sensitive item based on its BIV score
    best_item = data.loc[best_row_index]
    hidden_data = data[data.index != best_row_index]

    # Apply fuzzy logic, hiding the antecedents and consequents of the most sensitive rule
    hidden_data["antecedents"] = hidden_data["antecedents"].apply(
        lambda x: "Hidden" if x == best_item["antecedents"] else x
    )
    hidden_data["consequents"] = hidden_data["consequents"].apply(
        lambda x: "Hidden" if x == best_item["consequents"] else x
    )

    return hidden_data
