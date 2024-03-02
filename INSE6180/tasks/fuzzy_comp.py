import pandas as pd
import numpy as np


def compare_fuzzy_mining_results(original_rules_file, anonymized_rules_file):
    # Load the original and anonymized association rules
    original_rules = pd.read_csv(original_rules_file)
    anonymized_rules = pd.read_csv(anonymized_rules_file)

    # Calculate the number of association rules in each dataset
    original_rule_count = original_rules.shape[0]
    anonymized_rule_count = anonymized_rules.shape[0]

    # Calculate the percentage reduction in the number of association rules
    reduction_percentage = (
        (original_rule_count - anonymized_rule_count) / original_rule_count
    ) * 100

    # Calculate privacy preservation (Information Loss)
    information_loss_original = original_rules["BIV"].mean()
    information_loss_anonymized = anonymized_rules["BIV"].mean()
    information_loss_percentage = (
        (information_loss_original - information_loss_anonymized)
        / information_loss_original
    ) * 100

    # Check if the attribute is still disclosed in anonymized data
    attribute_disclosure_risk = (
        100.00 if "Hidden" not in anonymized_rules["antecedents"].values else 0.00
    )

    # Calculate additional statistics
    common_rule_count = len(
        original_rules[
            original_rules["antecedents"].isin(anonymized_rules["antecedents"])
        ]
    )
    reduction_sensitive_attributes = (
        (
            original_rules["antecedents"].nunique()
            - anonymized_rules["antecedents"].nunique()
        )
        / original_rules["antecedents"].nunique()
    ) * 100

    # Print the comparison results
    print(
        f"Privacy Preservation (Information Loss): {information_loss_percentage:.2f}%"
    )
    print(f"Attribute Disclosure Risk: {attribute_disclosure_risk:.2f}%")
    print(
        f"Percentage Reduction in the Number of Association Rules: {reduction_percentage:.2f}%"
    )
    print(f"Number of Association Rules in Original Data: {original_rule_count}")
    print(f"Number of Association Rules in Anonymized Data: {anonymized_rule_count}")
    print(f"Number of Common Association Rules: {common_rule_count}")
    print(
        f"Percentage Reduction in Sensitive Attributes: {reduction_sensitive_attributes:.2f}%\n"
    )
