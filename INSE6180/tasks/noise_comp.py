import pandas as pd


def compare_noisy_mining_results(
    original_noisy_itemsets_file,
    anonymized_noisy_itemsets_file,
    frequent_itemsets_file,
    frequent_itemsets_anonymized_file,
):
    """
    Compare frequent pattern mining results with added noise between the original and anonymized datasets.

    Args:
    - original_noisy_itemsets_file (str): Path to the CSV file containing frequent itemsets for the noisy original dataset.
    - anonymized_noisy_itemsets_file (str): Path to the CSV file containing frequent itemsets for the noisy anonymized dataset.
    - frequent_itemsets_file (str): Path to the CSV file containing frequent itemsets with support values for the original dataset.
    - frequent_itemsets_anonymized_file (str): Path to the CSV file containing frequent itemsets with support values for the anonymized dataset.

    Returns:
    - None
    """

    # Load frequent itemsets with noise from original dataset
    original_noisy_itemsets_df = pd.read_csv(original_noisy_itemsets_file)

    # Load frequent itemsets with noise from anonymized dataset
    anonymized_noisy_itemsets_df = pd.read_csv(anonymized_noisy_itemsets_file)

    # Load frequent itemsets with support values for original dataset
    frequent_itemsets_df = pd.read_csv(frequent_itemsets_file)

    # Load frequent itemsets with support values for anonymized dataset
    frequent_itemsets_anonymized_df = pd.read_csv(frequent_itemsets_anonymized_file)

    # Identify potentially fake itemsets in the original dataset
    original_potentially_fake_itemsets_count = sum(
        1
        for itemset in original_noisy_itemsets_df["itemsets"]
        if itemset not in frequent_itemsets_df["itemsets"].values
    )

    # Identify potentially fake itemsets in the anonymized dataset
    anonymized_potentially_fake_itemsets_count = sum(
        1
        for itemset in anonymized_noisy_itemsets_df["itemsets"]
        if itemset not in frequent_itemsets_anonymized_df["itemsets"].values
    )

    # Calculate privacy preservation (information loss)
    original_itemsets_count = len(original_noisy_itemsets_df)
    anonymized_itemsets_count = len(anonymized_noisy_itemsets_df)
    common_itemsets_count = len(
        set(original_noisy_itemsets_df["itemsets"]).intersection(
            anonymized_noisy_itemsets_df["itemsets"]
        )
    )
    original_itemset_disclosure_risk = (
        1 - common_itemsets_count / original_itemsets_count
    ) * 100
    anonymized_itemset_disclosure_risk = (
        1 - common_itemsets_count / anonymized_itemsets_count
    ) * 100
    information_loss = (
        1 - anonymized_itemset_disclosure_risk / original_itemset_disclosure_risk
    ) * 100
    reduction_sensitive_itemsets_percentage = (
        1 - anonymized_itemsets_count / original_itemsets_count
    ) * 100

    # Calculate utility of data mining results
    common_itemsets = set(original_noisy_itemsets_df["itemsets"]).intersection(
        anonymized_noisy_itemsets_df["itemsets"]
    )
    utility_original = len(original_noisy_itemsets_df)
    utility_anonymized = len(anonymized_noisy_itemsets_df)
    common_utility = len(common_itemsets)

    # Calculate the percentage reduction in potentially fake itemsets
    reduction_percentage_original = (
        1
        - original_potentially_fake_itemsets_count / original_noisy_itemsets_df.shape[0]
    ) * 100

    reduction_percentage_anonymized = (
        1
        - anonymized_potentially_fake_itemsets_count
        / anonymized_noisy_itemsets_df.shape[0]
    ) * 100

    # Print the comparison results
    print("Privacy Preservation (Information Loss):")
    print(f"Original Itemset Disclosure Risk: {original_itemset_disclosure_risk:.2f}%")
    print(
        f"Anonymized Itemset Disclosure Risk: {anonymized_itemset_disclosure_risk:.2f}%"
    )
    print(f"Information Loss due to Anonymization: {information_loss:.2f}%")
    print(
        f"Percentage Reduction in Sensitive Itemsets: {reduction_sensitive_itemsets_percentage:.2f}%\n"
    )

    print("Utility of Data Mining Results:")
    print(f"Number of Frequent Itemsets Generated (Original): {utility_original}")
    print(f"Number of Frequent Itemsets Generated (Anonymized): {utility_anonymized}")
    print(f"Number of Common Frequent Itemsets: {common_utility}")
    print("\nPotentially Fake Itemsets Comparison:")
    print(
        f"Original Potentially Fake Itemsets Count: {original_potentially_fake_itemsets_count}"
    )
    print(
        f"Anonymized Potentially Fake Itemsets Count: {anonymized_potentially_fake_itemsets_count}"
    )
    print(f"Percentage Reduction (Original): {reduction_percentage_original:.2f}%")
    print(f"Percentage Reduction (Anonymized): {reduction_percentage_anonymized:.2f}%")
    print()
