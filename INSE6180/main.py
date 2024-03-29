from tasks.association_mining import association_mining_func
from tasks.fuzzy import fuzzy_mining_func
from tasks.frequent_mining import frequent_mining_func
from tasks.noise import frequent_pattern_mining_with_noise
from tasks.ppdp import PrivacyPreservingDataPublisher
from tasks.asso_min_comp import compare_association_rules
from tasks.fuzzy_comp import compare_fuzzy_mining_results
from tasks.freq_pattern_comp import compare_frequent_mining_results
from tasks.noise_comp import compare_noisy_mining_results
import warnings


def main():

    # Suppress warnings to ensure clean output
    warnings.filterwarnings("ignore", category=DeprecationWarning)

    # Define paths to datasets
    dataset_path = r"database\student-mat.csv"
    fuzzy_dataset_path = r"outputs\association_rules.csv"

    # Define sensitive features  for our experiment
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

    # Perform association rule mining and save results
    rules = association_mining_func(dataset_path)
    rules.to_csv("outputs/association_rules.csv", index=False)

    # Perform fuzzy association rule mining and save results
    fuzzy_data = fuzzy_mining_func(fuzzy_dataset_path)
    fuzzy_data.to_csv("outputs/hidden_association_rules.csv", index=False)

    # Perform frequent pattern mining and save results
    frequent_itemsets = frequent_mining_func(dataset_path)
    frequent_itemsets.to_csv("outputs/frequent_itemsets.csv", index=False)

    # Perform frequent pattern mining with added noise and save results
    frequent_patterns_with_noise = frequent_pattern_mining_with_noise(
        dataset_path, min_support=0.1, noise_level=0.1
    )
    frequent_patterns_with_noise.to_csv("outputs/noise_itemsets.csv", index=False)

    # Initialize and apply anonymization pre-processing using the class PPDP
    ppdp = PrivacyPreservingDataPublisher(dataset_path)

    # Apply anonymization methods
    ppdp.k_anonymize(k=2)  # Apply k-anonymity
    ppdp.suppress(["age"])  # Suppress 'age' column for privacy
    ppdp.permutation("paid")  # Shuffle 'paid' column values
    ppdp.suppress(["guardian"])  # Suppress 'guardian' column
    ppdp.publish()  # Generate the anonymized data

    # Repeat mining techniques on the anonymized dataset
    anonymized_dataset_path = r"outputs\anonymized_data.csv"
    anonymized_fuzzy_dataset_path = r"outputs\association_rules_anonymized.csv"

    # Perform association rule mining on anonymized data and save results
    rules = association_mining_func(anonymized_dataset_path)
    rules.to_csv("outputs/association_rules_anonymized.csv", index=False)

    # Perform fuzzy association rule mining on anonymized data and save results
    fuzzy_data = fuzzy_mining_func(anonymized_fuzzy_dataset_path)
    fuzzy_data.to_csv("outputs/hidden_association_rules_anonymized.csv", index=False)

    # Perform frequent pattern mining on anonymized data and save results
    frequent_itemsets = frequent_mining_func(anonymized_dataset_path)
    frequent_itemsets.to_csv("outputs/frequent_itemsets_anonymized.csv", index=False)

    # Perform frequent pattern mining with added noise on anonymized data and save results
    frequent_patterns_with_noise = frequent_pattern_mining_with_noise(
        anonymized_dataset_path, min_support=0.1, noise_level=0.1
    )
    frequent_patterns_with_noise.to_csv(
        "outputs/noise_itemsets_anonymized.csv", index=False
    )

    # Comparison of results before and after anonymization
    print(
        "***************************\nAssociation Rules Data Mining Comparison Results\n***************************"
    )

    compare_association_rules(
        fuzzy_dataset_path,
        r"outputs\association_rules_anonymized.csv",
        sensitive_attributes,
    )

    print(
        "***************************\nFuzzy Logic Association Rules Data Mining Comparison Results\n***************************"
    )

    compare_fuzzy_mining_results(
        r"outputs\hidden_association_rules.csv",
        r"outputs\hidden_association_rules_anonymized.csv",
        sensitive_attributes,
    )

    print(
        "***************************\nFrequent Itemsets Data Mining Comparison Results\n***************************"
    )
    compare_frequent_mining_results(
        r"outputs\frequent_itemsets.csv",
        r"outputs\frequent_itemsets_anonymized.csv",
        sensitive_attributes,
    )

    print(
        "***************************\nFrequent Itemsets with Added Noise Data Mining Comparison Results\n***************************"
    )

    compare_noisy_mining_results(
        r"outputs\noise_itemsets.csv",
        r"outputs\noise_itemsets_anonymized.csv",
        r"outputs\frequent_itemsets.csv",
        r"outputs\frequent_itemsets_anonymized.csv",
        sensitive_attributes,
    )


main()
