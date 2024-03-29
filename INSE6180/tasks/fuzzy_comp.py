import pandas as pd


def compare_fuzzy_mining_results(
    original_rules_file, anonymized_rules_file, sensitive_attributes
):
    # Load association rules from both datasets
    original_rules = pd.read_csv(original_rules_file)
    anonymized_rules = pd.read_csv(anonymized_rules_file)

    # Identify common rules between the two datasets for a direct comparison
    common_rules = pd.merge(
        original_rules,
        anonymized_rules,
        on=["antecedents", "consequents"],
        how="inner",
        suffixes=("_orig", "_anon"),
    )
    common_rule_count = len(common_rules)

    # Calculate the reduction in number of rules as a percentage
    original_rule_count = len(original_rules)
    anonymized_rule_count = len(anonymized_rules)
    reduction_percentage = (
        (original_rule_count - anonymized_rule_count) / original_rule_count
    ) * 100

    # Calculate the attribute disclosure risk by comparing the presence of sensitive attributes in rules
    original_sensitive_rules = original_rules[
        original_rules["antecedents"].str.contains(
            "|".join(sensitive_attributes), na=False
        )
    ]
    anonymized_sensitive_rules = anonymized_rules[
        anonymized_rules["antecedents"].str.contains(
            "|".join(sensitive_attributes), na=False
        )
    ]
    attribute_disclosure_risk = (
        (len(anonymized_sensitive_rules) / len(original_sensitive_rules)) * 100
        if len(original_sensitive_rules) > 0
        else 0
    )

    # Evaluate information loss by comparing the mean Best Information Value (BIV) before and after anonymization
    information_loss_original = original_rules["BIV"].mean()
    information_loss_anonymized = anonymized_rules["BIV"].mean()
    information_loss_percentage = (
        (
            (information_loss_original - information_loss_anonymized)
            / information_loss_original
        )
        * 100
        if information_loss_original > 0
        else 0
    )

    # Determine the reduction in rules with sensitive attributes
    reduction_sensitive_attributes = (
        (
            (len(original_sensitive_rules) - len(anonymized_sensitive_rules))
            / len(original_sensitive_rules)
        )
        * 100
        if len(original_sensitive_rules) > 0
        else 0
    )

    # Print the comparison results
    print(
        f"Privacy Preservation (Information Loss): {information_loss_percentage:.2f}%"
    )
    print(f"Attribute Disclosure Risk: {attribute_disclosure_risk:.2f}%")
    print(
        f"Percentage Reduction in the Number of Association Rules: {reduction_percentage:.2f}%"
    )
    print(
        f"Percentage Reduction in Sensitive Attributes: {reduction_sensitive_attributes:.2f}%\n"
    )
    print("Utility of Data Mining Results:")
    print(f"Number of Association Rules in Original Data: {original_rule_count}")
    print(f"Number of Association Rules in Anonymized Data: {anonymized_rule_count}")
    print(f"Number of Common Association Rules: {common_rule_count}\n")
