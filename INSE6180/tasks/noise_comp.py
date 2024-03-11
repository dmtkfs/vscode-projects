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

    Args:
    - original_noisy_itemsets_file (str): Path to the CSV containing itemsets from the noisy original dataset.
    - anonymized_noisy_itemsets_file (str): Path to the CSV containing itemsets from the noisy anonymized dataset.
    - frequent_itemsets_file (str): Path to the CSV containing itemsets from the original dataset without added noise.
    - frequent_itemsets_anonymized_file (str): Path to the CSV containing itemsets from the anonymized dataset without added noise.
    - sensitive_attributes (list): List of attributes considered sensitive.
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

    # Calculate disclosure risks and information loss
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

    information_loss = (
        (1 - anonymized_disclosure_risk / original_disclosure_risk) * 100
        if original_disclosure_risk
        else 0
    )

    # Calculate utility of data mining results
    common_itemsets = set(original_noisy_itemsets_df["itemsets"]).intersection(
        anonymized_noisy_itemsets_df["itemsets"]
    )
    common_itemset_count = len(common_itemsets)

    # Print results
    print(f"Original Potentially Fake Itemsets Count: {original_fake_count}")
    print(f"Anonymized Potentially Fake Itemsets Count: {anonymized_fake_count}")
    print(
        f"Number of Frequent Itemsets Generated (Original): {len(original_noisy_itemsets_df)}"
    )
    print(
        f"Number of Frequent Itemsets Generated (Anonymized): {len(anonymized_noisy_itemsets_df)}"
    )
    print(f"Number of Common Frequent Itemsets: {common_itemset_count}")
    print(f"Original Itemset Disclosure Risk: {original_disclosure_risk:.2f}%")
    print(f"Anonymized Itemset Disclosure Risk: {anonymized_disclosure_risk:.2f}%")
    print(f"Information Loss due to Anonymization: {information_loss:.2f}%")
    print()
