import pandas as pd
import numpy as np


def compare_association_rules(
    original_rules_file, anonymized_rules_file, sensitive_attributes
):
    # Load association rules
    original_rules = pd.read_csv(original_rules_file)
    anonymized_rules = pd.read_csv(anonymized_rules_file)

    # Calculate information loss
    def calculate_information_loss(original_rules, anonymized_rules):
        original_antecedents = set(original_rules["antecedents"].str.split(", ").sum())
        anonymized_antecedents = set(
            anonymized_rules["antecedents"].str.split(", ").sum()
        )
        original_consequents = set(original_rules["consequents"].str.split(", ").sum())
        anonymized_consequents = set(
            anonymized_rules["consequents"].str.split(", ").sum()
        )

        antecedents_loss = len(original_antecedents) - len(anonymized_antecedents)
        consequents_loss = len(original_consequents) - len(anonymized_consequents)

        total_loss = antecedents_loss + consequents_loss
        total_items = len(original_antecedents) + len(original_consequents)

        information_loss = (total_loss / total_items) * 100
        return information_loss

    information_loss = calculate_information_loss(original_rules, anonymized_rules)
    print(f"Privacy Preservation (Information Loss): {information_loss:.2f}%")

    # Calculate attribute disclosure risk
    def calculate_attribute_disclosure_risk(
        original_rules, anonymized_rules, sensitive_attributes
    ):
        original_sensitive_rules = original_rules[
            original_rules["antecedents"].str.contains("|".join(sensitive_attributes))
            | original_rules["consequents"].str.contains("|".join(sensitive_attributes))
        ]
        anonymized_sensitive_rules = anonymized_rules[
            anonymized_rules["antecedents"].str.contains("|".join(sensitive_attributes))
            | anonymized_rules["consequents"].str.contains(
                "|".join(sensitive_attributes)
            )
        ]

        attribute_disclosure_risk = (
            len(anonymized_sensitive_rules) / len(original_sensitive_rules)
        ) * 100
        reduction_percentage = (
            (len(original_sensitive_rules) - len(anonymized_sensitive_rules))
            / len(original_sensitive_rules)
        ) * 100
        return attribute_disclosure_risk, reduction_percentage

    attribute_disclosure_risk, reduction_percentage = (
        calculate_attribute_disclosure_risk(
            original_rules, anonymized_rules, sensitive_attributes
        )
    )
    print(f"Attribute disclosure risk: {attribute_disclosure_risk:.2f}%")
    print(f"Percentage reduction in sensitive attributes: {reduction_percentage:.2f}%")

    # Comparison of association rules
    original_rule_count = original_rules.shape[0]
    anonymized_rule_count = anonymized_rules.shape[0]
    print(f"Number of association rules in original data: {original_rule_count}")
    print(f"Number of association rules in anonymized data: {anonymized_rule_count}")

    # Find common rules between original and anonymized
    common_rules = pd.merge(
        original_rules, anonymized_rules, how="inner", on=["antecedents", "consequents"]
    )
    common_rule_count = common_rules.shape[0]

    # Calculate number of rules disappeared in anonymized data
    disappeared_rule_count = original_rule_count - common_rule_count

    # Calculate percentage reduction
    percentage_reduction = (disappeared_rule_count / original_rule_count) * 100

    # Summary of differences
    print(f"Number of common association rules: {common_rule_count}")
    print(
        f"Number of association rules disappeared in anonymized data: {disappeared_rule_count} ({percentage_reduction:.2f}% reduction)\n"
    )
