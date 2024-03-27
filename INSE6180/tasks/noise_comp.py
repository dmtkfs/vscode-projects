import pandas as pd


def compare_noisy_mining_results(
    original_noisy_itemsets_file,
    anonymized_noisy_itemsets_file,
    frequent_itemsets_file,
    frequent_itemsets_anonymized_file,
    sensitive_attributes,
):
    """
    Performs a comprehensive analysis comparing frequent itemset mining results
    between original and anonymized datasets, considering added noise.
    """
    # Load all datasets
    original_noisy_itemsets_df = pd.read_csv(original_noisy_itemsets_file)
    anonymized_noisy_itemsets_df = pd.read_csv(anonymized_noisy_itemsets_file)
    frequent_itemsets_df = pd.read_csv(frequent_itemsets_file)
    frequent_itemsets_anonymized_df = pd.read_csv(frequent_itemsets_anonymized_file)

    # Calculate potentially fake itemsets
    original_fake_count = len(
        set(original_noisy_itemsets_df["itemsets"])
        - set(frequent_itemsets_df["itemsets"])
    )
    anonymized_fake_count = len(
        set(anonymized_noisy_itemsets_df["itemsets"])
        - set(frequent_itemsets_anonymized_df["itemsets"])
    )

    # Function to calculate disclosure risk
    def disclosure_risk(itemsets_df):
        sensitive_count = itemsets_df[
            itemsets_df["itemsets"].apply(
                lambda x: any(attr in x for attr in sensitive_attributes)
            )
        ]["support"].sum()
        total_count = itemsets_df["support"].sum()
        return (sensitive_count / total_count * 100) if total_count else 0

    original_disclosure_risk = disclosure_risk(frequent_itemsets_df)
    anonymized_disclosure_risk = disclosure_risk(frequent_itemsets_anonymized_df)

    # Calculate information loss
    information_loss = (
        (1 - anonymized_disclosure_risk / original_disclosure_risk) * 100
        if original_disclosure_risk
        else 0
    )

    # Calculate the number of common frequent itemsets
    common_itemsets = set(original_noisy_itemsets_df["itemsets"]).intersection(
        anonymized_noisy_itemsets_df["itemsets"]
    )
    common_itemset_count = len(common_itemsets)

    # Calculate the percentage reduction in sensitive itemsets
    original_sensitive_itemsets = sum(
        original_noisy_itemsets_df["itemsets"].apply(
            lambda x: any(item in x for item in sensitive_attributes)
        )
    )
    anonymized_sensitive_itemsets = sum(
        anonymized_noisy_itemsets_df["itemsets"].apply(
            lambda x: any(item in x for item in sensitive_attributes)
        )
    )
    reduction_sensitive_itemsets_percentage = (
        (original_sensitive_itemsets - anonymized_sensitive_itemsets)
        / original_sensitive_itemsets
        * 100
        if original_sensitive_itemsets
        else 0
    )

    # Print results
    print(f"Privacy Preservation (Information Loss): {information_loss:.2f}%")
    print(f"Original Itemset Disclosure Risk: {original_disclosure_risk:.2f}%")
    print(f"Anonymized Itemset Disclosure Risk: {anonymized_disclosure_risk:.2f}%")
    print(
        f"Percentage Reduction in Sensitive Itemsets: {reduction_sensitive_itemsets_percentage:.2f}%\n"
    )
    print("Utility of Data Mining Results:")
    print(f"Original Potentially Fake Itemsets Count: {original_fake_count}")
    print(f"Anonymized Potentially Fake Itemsets Count: {anonymized_fake_count}")
    print(
        f"Number of Frequent Itemsets Generated (Original): {len(original_noisy_itemsets_df)}"
    )
    print(
        f"Number of Frequent Itemsets Generated (Anonymized): {len(anonymized_noisy_itemsets_df)}"
    )
    print(f"Number of Common Frequent Itemsets: {common_itemset_count}")

    print()
