import pandas as pd
import numpy as np


def k_anon_comp(original_dataset, anon_dataset):

    # Load datasets
    original_data = pd.read_csv(original_dataset, sep=";")
    anonymized_data = pd.read_csv(anon_dataset, sep=";")

    # Calculate k-anonymity
    def calculate_k_anonymity(dataset):
        quasi_identifiers = [
            "sex",
            "age",
            "address",
            "famsize",
            "Pstatus",
            "Medu",
            "Fedu",
        ]
        unique_combinations = dataset[quasi_identifiers].drop_duplicates()
        return len(unique_combinations)

    original_k_anonymity = calculate_k_anonymity(original_data)
    anonymized_k_anonymity = calculate_k_anonymity(anonymized_data)

    print("Original k-anonymity level:", original_k_anonymity)
    print("Anonymized k-anonymity level:", anonymized_k_anonymity)
    print("YOLO")
