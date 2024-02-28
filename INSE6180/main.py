from tasks.association_mining import association_mining_func


def main():
    # Define the path to your dataset
    dataset_path = r"database\student-mat.csv"

    # Perform association rule mining
    rules = association_mining_func(dataset_path)

    # Print the association rules
    print(rules)


main()
