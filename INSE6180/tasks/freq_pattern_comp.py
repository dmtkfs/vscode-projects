import pandas as pd


def compare_frequent_mining_results(
    original_itemsets_file, anonymized_itemsets_file, sensitive_attributes
):
    # Calculate disclosure risk of itemsets based on sensitive features
    def calculate_itemset_disclosure_risk(itemsets_df):
        disclosure_risk = sum(
            itemsets_df["itemsets"].apply(
                lambda x: any(item in x for item in sensitive_attributes)
            )
        )
        disclosure_risk_percentage = (disclosure_risk / len(itemsets_df)) * 100
        return disclosure_risk_percentage

    # Load itemsets from the appropriate files
    original_itemsets = pd.read_csv(original_itemsets_file)
    anonymized_itemsets = pd.read_csv(anonymized_itemsets_file)

    # Disclosure risk before and after anonymization
    original_itemset_disclosure_risk = calculate_itemset_disclosure_risk(
        original_itemsets
    )
    anonymized_itemset_disclosure_risk = calculate_itemset_disclosure_risk(
        anonymized_itemsets
    )

    # Identify itemsets that are missing post-anonymization with a mix support
    original_itemsets_high_support = original_itemsets[
        original_itemsets["support"] > 0.1
    ]
    missing_itemsets_with_high_support = len(
        original_itemsets_high_support[
            ~original_itemsets_high_support["itemsets"].isin(
                anonymized_itemsets["itemsets"]
            )
        ]
    )

    # Calculate information loss as a percentage
    information_loss = (
        missing_itemsets_with_high_support / len(original_itemsets_high_support)
    ) * 100

    # Counting frequent itemsets and comparison between original and anonymized datasets
    original_itemsets_count = len(original_itemsets)
    anonymized_itemsets_count = len(anonymized_itemsets)
    common_itemsets_count = len(
        set(original_itemsets["itemsets"]).intersection(anonymized_itemsets["itemsets"])
    )

    # Evaluate sensitive itemset reduction
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

    # Print comparison results
    print(f"Privacy Preservation (Information Loss): {information_loss:.2f}%")
    print(f"Original Itemset Disclosure Risk: {original_itemset_disclosure_risk:.2f}%")
    print(
        f"Anonymized Itemset Disclosure Risk: {anonymized_itemset_disclosure_risk:.2f}%"
    )
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
    print(f"Number of Common Frequent Itemsets: {common_itemsets_count}\n")
