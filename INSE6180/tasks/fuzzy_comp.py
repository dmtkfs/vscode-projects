import pandas as pd

# List of sensitive attributes
sensitive_attributes = [
    "age",
    "Medu",
    "Fedu",
    "traveltime",
    "studytime",
    "failures",
    "famrel",
    "freetime",
    "goout",
    "Dalc",
    "Walc",
    "health",
    "absences",
]


def compare_fuzzy_mining_results(
    original_rules_file, anonymized_rules_file, sensitive_attributes
):
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

    # Check if sensitive attributes are still disclosed in anonymized data
    original_sensitive_rules = original_rules[
        original_rules["antecedents"].str.contains("|".join(sensitive_attributes))
    ]
    anonymized_sensitive_rules = anonymized_rules[
        anonymized_rules["antecedents"].str.contains("|".join(sensitive_attributes))
    ]
    attribute_disclosure_risk = (
        len(anonymized_sensitive_rules) / len(original_sensitive_rules)
    ) * 100

    # Calculate the number of common association rules
    common_rule_count = len(
        original_rules[
            original_rules["antecedents"].isin(anonymized_rules["antecedents"])
        ]
    )

    # Calculate the percentage reduction in the number of sensitive attributes
    original_unique_antecedents = original_rules["antecedents"].nunique()
    anonymized_unique_antecedents = anonymized_rules["antecedents"].nunique()
    reduction_sensitive_attributes = (
        (original_unique_antecedents - anonymized_unique_antecedents)
        / original_unique_antecedents
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
        f"Percentage Reduction in Sensitive Attributes: {reduction_sensitive_attributes:.2f}%"
    )
    print()
