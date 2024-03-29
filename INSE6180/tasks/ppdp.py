import pandas as pd
import numpy as np


class PrivacyPreservingDataPublisher:
    def __init__(self, file_path):
        # Load the dataset from appropriate file with ';' as the delimiter
        self.data = pd.read_csv(file_path, sep=";")

    def k_anonymize(self, k):
        # Apply k-anonymity by generalizing quasi-identifiers
        # We chose columns 23 to 29
        quasi_identifiers = self.data.columns[23:29]
        for column in quasi_identifiers:
            self.data[column] = self.generalize(self.data[column], k)

    def generalize(self, column, k):
        # When the column is 'age', generalize it into ranges
        if column.name == "age":
            bins = [0]
            for i in range(k):
                bins.append((i + 1) * 25)
            bins.append(np.inf)
            labels = [f"{bins[i]}-{bins[i+1]-1}" for i in range(len(bins) - 1)]
            return pd.cut(column, bins=bins, labels=labels, right=False)
        elif pd.api.types.is_numeric_dtype(column):
            # If the column is numeric, generalize into k equal-width ranges
            min_val = column.min()
            max_val = column.max()
            step = (max_val - min_val) / k
            bins = [min_val + i * step for i in range(k + 1)]
            labels = [f"{bins[i]}-{bins[i+1]}" for i in range(k)]
            return pd.cut(column, bins=bins, labels=labels, right=False)
        else:
            # If the column is non-numeric, simply return the column
            return column

    def suppress(self, columns_to_suppress):
        # Replace values in specified columns to generate suppression
        for column in columns_to_suppress:
            if column in self.data.columns:
                self.data[column] = "*"

    def permutation(self, sensitive_attribute):
        # Shuffle the values of a sensitive attribute to prevent linkage
        # We ensure attribute values are treated as strings
        if sensitive_attribute in self.data.columns:
            self.data[sensitive_attribute] = self.data[sensitive_attribute].apply(str)
            self.data[sensitive_attribute] = np.random.permutation(
                self.data[sensitive_attribute]
            )

    def publish(self):
        # Generate the anonymized dataset and create a new file
        print(self.data)
        self.data.to_csv(
            "outputs/anonymized_data.csv", sep=";", index=False, header=True
        )
