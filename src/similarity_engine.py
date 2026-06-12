import pandas as pd


def find_similar_non_ucl_players(
    player_name,
    striker_data,
    model,
    X_scaled,
    n_neighbors=15
):

    player_match = striker_data[
        striker_data["Player"] == player_name
    ]

    if player_match.empty:
        raise ValueError(
            f"Player '{player_name}' not found."
        )

    player_index = player_match.index[0]

    distances, indices = model.kneighbors(
        [X_scaled[player_index]],
        n_neighbors=n_neighbors
    )

    similar_players = striker_data.iloc[
        indices[0]
    ].copy()

    similar_players["distance"] = distances[0]

    similar_players["similarity_score"] = (
        100 / (1 + similar_players["distance"])
    )

    hidden_targets = similar_players[
        similar_players["is_ucl_team"] == False
    ].copy()

    return hidden_targets.sort_values(
        "similarity_score",
        ascending=False
    )

from src.scouting_score import add_scouting_score


def find_best_replacements(
    player_name,
    striker_data,
    model,
    X_scaled,
    n_neighbors=15,
    top_n=5
):

    results = find_similar_non_ucl_players(
        player_name,
        striker_data,
        model,
        X_scaled,
        n_neighbors
    )

    scouting_results = add_scouting_score(results)

    return scouting_results.head(top_n)


def find_hidden_gems(
    striker_data,
    max_age=24,
    min_minutes=1200,
    top_n=10
):

    gems = striker_data.copy()

    gems = gems[
        (gems["is_ucl_team"] == False)
        & (gems["Age"] <= max_age)
        & (gems["Min"] >= min_minutes)
    ]

    gems = gems.sort_values(
        "Gls_per90",
        ascending=False
    )

    return gems.head(top_n)

