import pandas as pd
import numpy as np
from sklearn.utils import shuffle


class PrivacyPreservingDataPublisher:
    def __init__(self, file_path):
        self.data = pd.read_csv(file_path, sep=";")  # Specify the separator as ';'

    def k_anonymize(self, k):
        # Apply k-anonymity by generalizing quasi-identifiers
        # For simplicity, let's assume the first 4 columns are quasi-identifiers
        quasi_identifiers = self.data.columns[23:29]
        for column in quasi_identifiers:
            self.data[column] = self.generalize(self.data[column], k)

    def generalize(self, column, k):
        # If the column is 'age', generalize ages into ranges
        if column.name == "age":
            bins = [0]
            for i in range(k):
                bins.append((i + 1) * 25)
            bins.append(np.inf)
            labels = [f"{bins[i]}-{bins[i+1]-1}" for i in range(len(bins) - 1)]
            return pd.cut(column, bins=bins, labels=labels, right=False)
        else:
            # For other columns, generalize values into fewer categories
            if pd.api.types.is_numeric_dtype(column):
                # If the column is numeric, generalize into k categories
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
        # Apply suppression by replacing values with '*'
        for column in columns_to_suppress:
            if column in self.data.columns:
                self.data[column] = "*"

    def permutation(self, sensitive_attribute):
        # Apply permutation by shuffling sensitive attribute values within each group
        if sensitive_attribute in self.data.columns:
            self.data[sensitive_attribute] = self.data[sensitive_attribute].apply(str)
            self.data[sensitive_attribute] = np.random.permutation(
                self.data[sensitive_attribute]
            )

    def publish(self):
        # Publish the anonymized data
        print(self.data)
        self.data.to_csv(
            "outputs/anonymized_data.csv", sep=";", index=False, header=True
        )
