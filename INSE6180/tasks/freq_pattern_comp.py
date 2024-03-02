import pandas as pd


def compare_frequent_mining_results(
    original_itemsets_file, anonymized_itemsets_file, sensitive_attributes
):
    """
    Compare frequent itemsets data mining results between the original and anonymized datasets.

    Args:
    - original_itemsets_file (str): Path to the CSV file containing frequent itemsets for the original dataset.
    - anonymized_itemsets_file (str): Path to the CSV file containing frequent itemsets for the anonymized dataset.

    Returns:
    - None
    """

    # Function to calculate itemset disclosure risk
    def calculate_itemset_disclosure_risk(itemsets_df):
        disclosure_risk = sum(
            itemsets_df["itemsets"].apply(
                lambda x: any(item in x for item in sensitive_attributes)
            )
        )
        disclosure_risk_percentage = (disclosure_risk / len(itemsets_df)) * 100
        return disclosure_risk_percentage

    # Load the original and anonymized frequent itemsets
    original_itemsets = pd.read_csv(original_itemsets_file)
    anonymized_itemsets = pd.read_csv(anonymized_itemsets_file)

    # Calculate itemset disclosure risk
    original_itemset_disclosure_risk = calculate_itemset_disclosure_risk(
        original_itemsets
    )
    anonymized_itemset_disclosure_risk = calculate_itemset_disclosure_risk(
        anonymized_itemsets
    )

    # Calculate information loss due to anonymization
    original_itemsets_high_support = original_itemsets[
        original_itemsets["support"] > 0.1
    ]  # Adjust the threshold as needed
    missing_itemsets_with_high_support = len(
        original_itemsets_high_support[
            ~original_itemsets_high_support["itemsets"].isin(
                anonymized_itemsets["itemsets"]
            )
        ]
    )
    information_loss = (
        missing_itemsets_with_high_support / len(original_itemsets_high_support)
    ) * 100

    # Calculate the number of frequent itemsets generated
    original_itemsets_count = len(original_itemsets)
    anonymized_itemsets_count = len(anonymized_itemsets)

    # Calculate the number of common frequent itemsets
    common_itemsets_count = len(
        set(original_itemsets["itemsets"]).intersection(anonymized_itemsets["itemsets"])
    )

    # Calculate the percentage reduction in sensitive itemsets
    original_sensitive_itemsets_count = original_itemsets[
        original_itemsets["itemsets"].apply(
            lambda x: any(item in x for item in sensitive_attributes)
        )
    ].shape[0]
    anonymized_sensitive_itemsets_count = anonymized_itemsets[
        anonymized_itemsets["itemsets"].apply(
            lambda x: any(item in x for item in sensitive_attributes)
        )
    ].shape[0]
    reduction_sensitive_itemsets_percentage = (
        (original_sensitive_itemsets_count - anonymized_sensitive_itemsets_count)
        / original_sensitive_itemsets_count
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
    print(
        f"Number of Frequent Itemsets Generated (Original): {original_itemsets_count}"
    )
    print(
        f"Number of Frequent Itemsets Generated (Anonymized): {anonymized_itemsets_count}"
    )
    print(f"Number of Common Frequent Itemsets: {common_itemsets_count}")
    print()
