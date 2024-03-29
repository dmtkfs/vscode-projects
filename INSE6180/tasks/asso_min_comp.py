import pandas as pd
import numpy as np


def compare_association_rules(
    original_rules_file, anonymized_rules_file, sensitive_attributes
):
    # Load the association rules from the appropriate files
    original_rules = pd.read_csv(original_rules_file)
    anonymized_rules = pd.read_csv(anonymized_rules_file)

    # Calculate information loss based on differences in antecedents and consequents between datasets
    def calculate_information_loss(original_rules, anonymized_rules):
        # Extract and compare the unique elements in antecedents and consequents
        original_antecedents = set(original_rules["antecedents"].str.split(", ").sum())
        anonymized_antecedents = set(
            anonymized_rules["antecedents"].str.split(", ").sum()
        )
        original_consequents = set(original_rules["consequents"].str.split(", ").sum())
        anonymized_consequents = set(
            anonymized_rules["consequents"].str.split(", ").sum()
        )

        # Calculate losses and then the overall information loss as a percentage
        antecedents_loss = len(original_antecedents) - len(anonymized_antecedents)
        consequents_loss = len(original_consequents) - len(anonymized_consequents)

        total_loss = antecedents_loss + consequents_loss
        total_items = len(original_antecedents) + len(original_consequents)

        information_loss = (total_loss / total_items) * 100
        return information_loss

    # Calculate and print information from anonymization
    information_loss = calculate_information_loss(original_rules, anonymized_rules)
    print(f"Privacy Preservation (Information Loss): {information_loss:.2f}%")

    # Calculate attribute disclosure risk based on the presence of sensitive attributes in the rules
    def calculate_attribute_disclosure_risk(
        original_rules, anonymized_rules, sensitive_attributes
    ):
        # Identify rules with  sensitive attributes
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

        # Calculate disclosure risk and sensitive rule reduction as percentages
        attribute_disclosure_risk = (
            len(anonymized_sensitive_rules) / len(original_sensitive_rules)
        ) * 100
        reduction_percentage = (
            (len(original_sensitive_rules) - len(anonymized_sensitive_rules))
            / len(original_sensitive_rules)
        ) * 100
        return attribute_disclosure_risk, reduction_percentage

    # Calculate and print attribute disclosure risk and sensitive attribute reduction
    attribute_disclosure_risk, reduction_percentage = (
        calculate_attribute_disclosure_risk(
            original_rules, anonymized_rules, sensitive_attributes
        )
    )
    print(f"Attribute Disclosure Risk: {attribute_disclosure_risk:.2f}%")
    print(f"Percentage Reduction in Sensitive Attributes: {reduction_percentage:.2f}%")

    # Compare the number of rules in both datasets
    common_rules = pd.merge(
        original_rules, anonymized_rules, how="inner", on=["antecedents", "consequents"]
    )
    common_rule_count = common_rules.shape[0]
    disappeared_rule_count = original_rules.shape[0] - common_rule_count
    percentage_reduction = (disappeared_rule_count / original_rules.shape[0]) * 100

    # Print the comparison results
    print(
        f"Percentage Reduction in the Number of Association Rules: {percentage_reduction:.2f}%\n"
    )
    print("Utility of Data Mining Results:")
    print(f"Number of Association Rules in Original Data: {original_rules.shape[0]}")
    print(
        f"Number of Association Rules in Anonymized Data: {anonymized_rules.shape[0]}"
    )
    print(f"Number of Common Association Rules: {common_rule_count}\n")
