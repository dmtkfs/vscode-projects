import pandas as pd


def fuzzy_mining_func(dataset_path):
    df = pd.read_csv(dataset_path)
    data = df.copy()

    # Define Fuzzy Membership Functions for hiding level
    def membership_function(x):
        if x >= 70:
            return "very high"
        elif x >= 38:
            return "high"
        elif x >= 17:
            return "medium"
        else:
            return "low"

    # Calculate Membership Scores for Confidence Values
    def calculate_membership_scores(data):
        membership_scores = []
        for _, row in data.iterrows():
            score = membership_function(row["confidence"])
            membership_scores.append(score)
        return membership_scores

    # Determine Hiding Degree Based on Confidence Values
    def determine_hiding_degree(membership_scores):
        hiding_degree = []
        for score in membership_scores:
            if score == "very high":
                hiding_degree.append("hide")
            elif score == "high":
                hiding_degree.append("hide")
            elif score == "medium":
                hiding_degree.append("partial_hide")
            else:
                hiding_degree.append("no_hide")
        return hiding_degree

    # Hide Association Rules Based on Hiding Degree
    def hide_association_rules(data, hiding_degree):
        hidden_data = data.copy()
        for idx, degree in enumerate(hiding_degree):
            if degree == "hide":
                hidden_data.at[idx, "antecedents"] = "***HIDDEN***"
                hidden_data.at[idx, "consequents"] = "***HIDDEN***"
            elif degree == "partial_hide":
                # Adjust hiding degree for medium scores (you can customize this based on your needs)
                hidden_data.at[idx, "antecedents"] = "***PARTIAL HIDDEN***"
                hidden_data.at[idx, "consequents"] = "***PARTIAL HIDDEN***"
        return hidden_data

    # Step 1: Calculate Membership Scores for Confidence Values
    membership_scores = calculate_membership_scores(data)

    # Step 2: Determine Hiding Degree Based on Confidence Values
    hiding_degree = determine_hiding_degree(membership_scores)

    # Step 3: Hide Association Rules Based on Hiding Degree
    hidden_data = hide_association_rules(data, hiding_degree)

    print(hidden_data)

    return hidden_data
