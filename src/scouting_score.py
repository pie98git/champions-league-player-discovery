def add_scouting_score(results):

    results = results.copy()

    results["age_score"] = results["Age"].apply(
        lambda x: 100 if x <= 23 else
                  85 if x <= 26 else
                  70 if x <= 29 else
                  50
    )

    results["minutes_score"] = (
        results["Min"] / results["Min"].max()
    ) * 100

    results["scouting_score"] = (
    0.75 * results["similarity_score"]
    + 0.15 * results["minutes_score"]
    + 0.10 * results["age_score"]
)

    return results.sort_values(
        "scouting_score",
        ascending=False
    )