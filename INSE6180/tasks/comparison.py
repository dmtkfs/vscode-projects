import pandas as pd


def compare_privacy_preservation(original_data_file, anonymized_data_file):
    # Load original and anonymized datasets
    original_data = pd.read_csv(original_data_file, sep=";")
    anonymized_data = pd.read_csv(anonymized_data_file, sep=";")

    # Calculate percentage of suppressed cells in the anonymized dataset
    total_cells = original_data.shape[0] * original_data.shape[1]
    suppressed_cells = (anonymized_data == "*").sum().sum()
    suppression_percentage = round((suppressed_cells / total_cells) * 100, 3)

    return suppression_percentage


def compare_results_accuracy_utility(original_results_file, anonymized_results_file):
    # Load original and anonymized results files
    original_results = pd.read_csv(original_results_file)
    anonymized_results = pd.read_csv(anonymized_results_file)

    # Calculate percentage difference in number of association rules or frequent itemsets
    original_count = len(original_results)
    anonymized_count = len(anonymized_results)
    difference_percentage = round(
        ((anonymized_count - original_count) / original_count) * 100, 3
    )

    return difference_percentage
