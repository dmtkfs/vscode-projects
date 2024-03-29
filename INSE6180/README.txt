Overview of Files
******************

1/ `main.py`
This file does the main work for data mining and privacy-preserving steps. It coordinates the processes of association rule mining, 
fuzzy mining, frequent pattern mining, and privacy-preserving data publishing. Furthermore, it prints the results for our project.

2/ `association_mining.py`
Performs association rule mining using the Apriori algorithm to find associations between items in the datasets.

3/ `fuzzy.py`
Implements a fuzzy logic approach to minimize the visibility of sensitive association rules by modifying the datasets accordingly.

4/ `frequent_mining.py`
Conducts frequent itemset mining on the datasets to identify frequently occurring itemsets based on a given support threshold.

5/ `noise.py`
Adds noise to the datasets as a method of privacy preservation, specifically targeting sensitive itemsets.

6/ `ppdp.py`
Defines a class for privacy-preserving dataset generation, applying techniques such as k-anonymity, suppression, and permutation 
to protect chosen features.

7/ `asso_min_comp.py`, `fuzzy_comp.py`, `freq_pattern_comp.py`, `noise_comp.py`
These files contain functions to compare the results of data mining tasks (association rule mining, fuzzy logic-based mining, 
frequent pattern mining, and noise-added mining) between the original and anonymized datasets, evaluating the impact of 
privacy-preserving techniques and output utility.

Functions and Library Usage
****************************

1/ `main.py`
- Function: main(): 
  - Purpose: The main function coordinates the workflow, including data loading, mining, applying privacy techniques, 
    and evaluating the outcomes. It performs the following:
    - Suppresses warnings, particularly `DeprecationWarning`, to clean up the output.
    - Specifies dataset paths and lists chosen sensitive attributes.
    - Executes association rule mining and saves the results.
    - Performs fuzzy logic-based mining to obscure sensitive rules and saves the results.
    - Conducts frequent pattern mining to identify common itemsets and saves the results.
    - Adds noise to the datasets and mines  for frequent patterns, saving the results.
    - Initializes a privacy-preserving data publisher (`PPDP`) and applies various anonymization techniques, including k-anonymity, 
      suppression, and permutation, to the data.
    - Publishes the anonymized dataset and repeats the mining processes on this dataset to compare the impact of the privacy-preserving 
      methods on data utility and privacy.
    - Compares the results of data mining operations before and after anonymization across the different methods, evaluating the 
      trade-offs between data utility and privacy.
  - Imported Libraries:
    - `pandas`: Used for data manipulation and IO operations, such as reading CSV files and saving results.
    - From `tasks` module, various functions and a class are imported to perform specific data mining tasks and comparisons:
      - `association_mining`, `fuzzy`, `frequent_mining`, and `noise` modules contain functions for executing data mining techniques.
      - `ppdp` module defines a class for applying privacy-preserving methods to the dataset.
      - `asso_min_comp`, `fuzzy_comp`, `freq_pattern_comp`, and `noise_comp` modules provide functions for comparing data mining 
        results pre and post anonymization to evaluate the impact of privacy-preserving techniques.
    - `warnings`: Utilized to suppress specific types of warnings that might clutter the console output, enhancing readability.

2/ `association_mining.py`
- Function: association_mining_func(dataset_path)
  - Purpose: Loads a dataset and performs association rule mining to discover interesting relationships between variables in large databases.
  - Imported Libraries:
    - `pandas`: For data manipulation and analysis.
    - `mlxtend.frequent_patterns`: Provides the apriori and association_rules functions for conducting association rule mining.

3/ `fuzzy.py`
- Function: `fuzzy_mining_func(data_file_path, alpha1=0.5, alpha2=0.5)`
  - Purpose: Applies fuzzy logic to handle uncertainties in association rule mining, aiming to minimize the visibility of sensitive rules by 
    altering their representation.
  - Imported Libraries:
    - `pandas`: Used for loading and manipulating the dataset.
    - `numpy`: Provides support for mathematical operations, specifically for calculations involving Information Strength (IS), 
      Degree of Confidence (DOC), and Best Information Value (BIV).

4/ `frequent_mining.py`
- Function: `frequent_mining_func(dataset_path, min_support=0.1)`
  - Purpose: Identifies frequent itemsets in the dataset that meet a specified minimum support threshold using the Apriori algorithm.
  - Imported Libraries:
    - `pandas`: For data manipulation and analysis.
    - `numpy`: For numerical operations.
    - `mlxtend.frequent_patterns`: Provides the `apriori` method for frequent itemset mining.

5/ `noise.py`
- Function: `frequent_pattern_mining_with_noise(dataset_path, min_support=0.1, noise_level=0.1)`
  - Purpose: Enhances data privacy by injecting noise into the dataset before performing frequent pattern mining, aiming to obfuscate 
    sensitive itemsets.
  - Imported Libraries:
    - `pandas`: For data manipulation.
    - `numpy`: Used for numerical calculations, especially in the generation of noise and selection of indices for noise addition.
    - `mlxtend.frequent_patterns`: Utilizes the `apriori` method to conduct frequent pattern mining on the modified dataset.

6/ `ppdp.py`
- Class: `PrivacyPreservingDataPublisher`
  - Purpose: Offers methods for applying various privacy-preserving techniques such as k-anonymity, suppression, and permutation on a dataset.
  - Imported Libraries:
    - `pandas`: For loading and manipulating the dataset.
    - `numpy`: Used for mathematical operations, particularly in the permutation method to shuffle sensitive attribute values.

7/ `asso_min_comp.py`, `fuzzy_comp.py`, `freq_pattern_comp.py`, `noise_comp.py`
- General Purpose: These files contain functions designed to compare the results of different data mining approaches (association rule mining, 
  fuzzy mining, frequent pattern mining, and noise-added mining) before and after anonymization. They evaluate the effectiveness and impact of 
  privacy-preserving measures on the utility and privacy of data mining results.
- Imported Libraries:
  - `pandas`: Central to all comparison functions for loading, manipulating, and merging datasets to calculate metrics such as information loss, 
    disclosure risk, and the reduction in the number of (sensitive) rules or itemsets.