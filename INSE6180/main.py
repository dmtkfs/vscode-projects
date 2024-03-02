import pandas as pd
from tasks.association_mining import association_mining_func
from tasks.fuzzy import fuzzy_mining_func
from tasks.frequent_mining import frequent_mining_func
from tasks.noise import frequent_pattern_mining_with_noise
from tasks.ppdp import PrivacyPreservingDataPublisher
from tasks.comparison import compare_privacy_preservation
from tasks.comparison import compare_results_accuracy_utility
from tasks.asso_min_comp import compare_data_privacy_and_mining
from tasks.fuzzy_comp import compare_fuzzy_mining_results
from tasks.freq_pattern_comp import compare_frequent_mining_results
import warnings


def main():

    # Suppress DeprecationWarning
    warnings.filterwarnings("ignore", category=DeprecationWarning)

    # dataset paths
    dataset_path = r"database\student-mat.csv"
    fuzzy_dataset_path = r"outputs\association_rules.csv"

    # execute association rule mining
    rules = association_mining_func(dataset_path)

    # save association rules results table
    rules.to_csv("outputs/association_rules.csv", index=False)

    # execute fuzzy mining
    fuzzy_data = fuzzy_mining_func(fuzzy_dataset_path)

    # save the fuzzy mining results table
    fuzzy_data.to_csv("outputs/hidden_association_rules.csv", index=False)

    # execute frequent pattern mining
    frequent_itemsets = frequent_mining_func(dataset_path)

    # save the frequent pattern mining results table
    frequent_itemsets.to_csv("outputs/frequent_itemsets.csv", index=False)

    # execute frequent pattern mining with noise
    frequent_patterns_with_noise = frequent_pattern_mining_with_noise(
        dataset_path, min_support=0.1, noise_level=0.1
    )

    # save the noise mining results table
    frequent_patterns_with_noise.to_csv("outputs/noise_itemsets.csv", index=False)

    # Initialize PPDP
    ppdp = PrivacyPreservingDataPublisher(dataset_path)

    # Apply anonymization operations
    ppdp.k_anonymize(k=2)
    ppdp.suppress(["age"])  # Example: Suppressing identifier
    # Permutation and suppression operations can also be applied if needed
    ppdp.permutation("paid")
    ppdp.suppress(["guardian"])

    # Publish the anonymized data
    ppdp.publish()

    # rerun with anonymized data now
    # dataset paths
    anonymized_dataset_path = r"outputs\anonymized_data.csv"
    anonymized_fuzzy_dataset_path = r"outputs\association_rules_anonymized.csv"

    # execute association rule mining
    rules = association_mining_func(anonymized_dataset_path)

    # save association rules results table
    rules.to_csv("outputs/association_rules_anonymized.csv", index=False)

    # execute fuzzy mining
    fuzzy_data = fuzzy_mining_func(anonymized_fuzzy_dataset_path)

    # save the fuzzy mining results table
    fuzzy_data.to_csv("outputs/hidden_association_rules_anonymized.csv", index=False)

    # execute frequent pattern mining
    frequent_itemsets = frequent_mining_func(anonymized_dataset_path)

    # save the frequent pattern mining results table
    frequent_itemsets.to_csv("outputs/frequent_itemsets_anonymized.csv", index=False)

    # execute frequent pattern mining with noise
    frequent_patterns_with_noise = frequent_pattern_mining_with_noise(
        anonymized_dataset_path, min_support=0.1, noise_level=0.1
    )

    # save the noise mining results table
    frequent_patterns_with_noise.to_csv(
        "outputs/noise_itemsets_anonymized.csv", index=False
    )
    # Beta Comparison:
    privacy_percentage = compare_privacy_preservation(
        r"database\student-mat.csv", r"outputs\anonymized_data.csv"
    )
    print(
        f"\n============================================================\nPrivacy preservation percentage: {privacy_percentage}%\n============================================================"
    )

    accuracy_percentage = compare_results_accuracy_utility(
        r"outputs\association_rules.csv", r"outputs\association_rules_anonymized.csv"
    )
    print(
        f"Results accuracy and utility percentage difference: {accuracy_percentage}%\n============================================================\n"
    )
    # First comparison for association rules data mining:
    print(
        "\n***************************\nAssociation Rules Data Mining Comparison Results\n***************************"
    )

    compare_data_privacy_and_mining(
        dataset_path,
        anonymized_dataset_path,
        fuzzy_dataset_path,
        r"outputs\association_rules_anonymized.csv",
    )

    # Second comparison for association rules with fuzzy logic data mining:
    print(
        "***************************\nFuzzy Logic Association Rules Data Mining Comparison Results\n***************************"
    )

    compare_fuzzy_mining_results(
        r"outputs\hidden_association_rules.csv",
        r"outputs\hidden_association_rules_anonymized.csv",
    )

    # Print ranges and their categories
    print(f"@@@" * 30)
    print("Ranges and Categories:")
    print("Information Loss:")
    print("Low: Information loss < 5%")
    print("Moderate: 5% ≤ Information loss < 10%")
    print("High: Information loss ≥ 10%\n")
    print("Attribute Disclosure Risk:")
    print("Low: Attribute disclosure risk ≤ 50%")
    print("Moderate: 50% < Attribute disclosure risk < 80%")
    print("High: Attribute disclosure risk ≥ 80%\n")
    print("Number of Association Rules:")
    print("Significant Impact: > 50% reduction in the number of association rules")
    print(f"@@@" * 30)
    print()

    # Third comparison for frequent itemsets:
    print(
        "***************************\nFrequent Itemsets Data Mining Comparison Results\n***************************"
    )
    compare_frequent_mining_results(
        r"outputs\frequent_itemsets.csv", r"outputs\frequent_itemsets_anonymized.csv"
    )


main()
