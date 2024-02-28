import pandas as pd
import numpy as np


def fuzzy_mining_func(data_file_path, alpha1, alpha2):
    # Step 1: Load the data
    data = pd.read_csv(data_file_path)

    # Step 2: Compute Nj for each item
    Nj_dict = data["antecedents"].value_counts().to_dict()
    data["Nj"] = data["antecedents"].map(Nj_dict)

    # Step 3: Compute IS for each row
    data["IS"] = (data["Nj"] * data["support"]) / data["antecedent support"]

    # Step 4: Compute DOC for each row
    data["DOC"] = np.sqrt((data["confidence"] - data["consequent support"]) ** 2)

    # Step 5: Compute BIV for each row
    data["BIV"] = alpha1 * data["IS"] + alpha2 * data["DOC"]

    # Step 6: Find the row with the minimum BIV
    best_row_index = data["BIV"].idxmin()

    # Step 7: Hide the data based on the best row
    best_item = data.loc[best_row_index]
    hidden_data = data[data.index != best_row_index]

    # Step 8: Apply fuzzy logic to hide the best item
    hidden_data["antecedents"] = hidden_data["antecedents"].apply(
        lambda x: "Hidden" if x == best_item["antecedents"] else x
    )
    hidden_data["consequents"] = hidden_data["consequents"].apply(
        lambda x: "Hidden" if x == best_item["consequents"] else x
    )

    return hidden_data
